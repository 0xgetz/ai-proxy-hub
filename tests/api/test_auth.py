from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from api.app import create_app
from api.dependencies import get_settings
from api.runtime import AppRuntime
from config.security import (
    ensure_network_bind_is_authenticated,
    normalize_presented_api_token,
)
from config.settings import Settings

app = create_app()


def test_anthropic_auth_token_required_and_accepts_x_api_key():
    client = TestClient(app)
    settings = Settings()
    settings.anthropic_auth_token = "s3cr3t"
    app.dependency_overrides[get_settings] = lambda: settings

    payload = {
        "model": "claude-3-sonnet",
        "messages": [{"role": "user", "content": "hello"}],
    }

    with patch("api.routes.get_token_count", return_value=1):
        # No header -> 401
        r = client.post("/v1/messages/count_tokens", json=payload)
        assert r.status_code == 401

        # X-API-Key header -> 200
        r = client.post(
            "/v1/messages/count_tokens", json=payload, headers={"X-API-Key": "s3cr3t"}
        )
        assert r.status_code == 200
        assert r.json()["input_tokens"] == 1

    app.dependency_overrides.clear()


def test_anthropic_auth_token_accepts_bearer_authorization():
    client = TestClient(app)
    settings = Settings()
    settings.anthropic_auth_token = "b3artoken"
    app.dependency_overrides[get_settings] = lambda: settings

    payload = {
        "model": "claude-3-sonnet",
        "messages": [{"role": "user", "content": "hello"}],
    }

    with patch("api.routes.get_token_count", return_value=2):
        # Authorization Bearer -> 200
        r = client.post(
            "/v1/messages/count_tokens",
            json=payload,
            headers={"Authorization": "Bearer b3artoken"},
        )
        assert r.status_code == 200
        assert r.json()["input_tokens"] == 2

    app.dependency_overrides.clear()


def test_anthropic_auth_token_normalizes_configured_whitespace():
    client = TestClient(app)
    settings = Settings()
    settings.anthropic_auth_token = "  spaced-token  \n"
    app.dependency_overrides[get_settings] = lambda: settings

    payload = {
        "model": "claude-3-sonnet",
        "messages": [{"role": "user", "content": "hello"}],
    }

    with patch("api.routes.get_token_count", return_value=3):
        r = client.post(
            "/v1/messages/count_tokens",
            json=payload,
            headers={"Authorization": "Bearer spaced-token"},
        )
        assert r.status_code == 200
        assert r.json()["input_tokens"] == 3

    app.dependency_overrides.clear()


def test_anthropic_auth_token_applies_to_models_endpoint():
    client = TestClient(app)
    settings = Settings()
    settings.anthropic_auth_token = "models-token"
    app.dependency_overrides[get_settings] = lambda: settings

    r = client.get("/v1/models")
    assert r.status_code == 401

    r = client.get("/v1/models", headers={"X-API-Key": "models-token"})
    assert r.status_code == 200
    assert "data" in r.json()

    app.dependency_overrides.clear()


def test_root_get_requires_auth_but_root_probes_are_public():
    client = TestClient(app)
    settings = Settings()
    settings.anthropic_auth_token = "root-token"
    app.dependency_overrides[get_settings] = lambda: settings

    response = client.get("/")
    assert response.status_code == 401

    head = client.head("/")
    assert head.status_code == 204
    assert head.headers["Allow"] == "GET, HEAD, OPTIONS"

    options = client.options("/")
    assert options.status_code == 204
    assert options.headers["Allow"] == "GET, HEAD, OPTIONS"

    app.dependency_overrides.clear()


def test_presented_token_strips_model_suffix_only_when_configured_has_no_colon():
    assert (
        normalize_presented_api_token("secret:claude-sonnet", "secret") == "secret"
    )
    # Configured tokens that contain ":" must match in full (no strip).
    assert (
        normalize_presented_api_token("ab:cd", "ab:cd") == "ab:cd"
    )
    assert normalize_presented_api_token("ab:cd:extra", "ab:cd") == "ab:cd:extra"


def test_auth_accepts_configured_token_containing_colon():
    client = TestClient(app)
    settings = Settings()
    settings.anthropic_auth_token = "part1:part2"
    app.dependency_overrides[get_settings] = lambda: settings

    payload = {
        "model": "claude-3-sonnet",
        "messages": [{"role": "user", "content": "hello"}],
    }

    with patch("api.routes.get_token_count", return_value=1):
        r = client.post(
            "/v1/messages/count_tokens",
            json=payload,
            headers={"X-API-Key": "part1:part2"},
        )
        assert r.status_code == 200

        # Colon suffix is NOT stripped when configured token has a colon.
        r = client.post(
            "/v1/messages/count_tokens",
            json=payload,
            headers={"X-API-Key": "part1"},
        )
        assert r.status_code == 401

    app.dependency_overrides.clear()


def test_network_bind_requires_auth_token():
    ensure_network_bind_is_authenticated(
        Settings.model_construct(host="127.0.0.1", anthropic_auth_token="")
    )
    ensure_network_bind_is_authenticated(
        Settings.model_construct(host="0.0.0.0", anthropic_auth_token="strong-token")
    )
    with pytest.raises(RuntimeError, match="ANTHROPIC_AUTH_TOKEN is required"):
        ensure_network_bind_is_authenticated(
            Settings.model_construct(host="0.0.0.0", anthropic_auth_token="")
        )


@pytest.mark.asyncio
async def test_startup_rejects_unauthenticated_non_loopback_bind():
    app = create_app(lifespan_enabled=False)
    settings = Settings.model_construct(host="0.0.0.0", anthropic_auth_token="")
    runtime = AppRuntime.for_app(app, settings=settings)
    with pytest.raises(RuntimeError, match="ANTHROPIC_AUTH_TOKEN is required"):
        await runtime.startup()
