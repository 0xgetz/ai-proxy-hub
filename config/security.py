"""Bind / auth security helpers for the local AI Gateway server."""

from __future__ import annotations

import ipaddress

from config.settings import Settings


def is_loopback_bind_host(host: str) -> bool:
    """Return True when ``host`` only accepts local machine connections."""
    normalized = (host or "").strip().strip("[]").lower()
    if not normalized:
        return False
    if normalized in {"localhost", "127.0.0.1", "::1"}:
        return True
    try:
        return ipaddress.ip_address(normalized).is_loopback
    except ValueError:
        # Unknown hostnames are treated as network-exposed.
        return False


def ensure_network_bind_is_authenticated(settings: Settings) -> None:
    """Refuse non-loopback binds when ``ANTHROPIC_AUTH_TOKEN`` is empty.

    Local-only defaults (``127.0.0.1`` / ``::1``) may run without a proxy token for
    developer convenience. Binding ``0.0.0.0`` / ``::`` / a public address without
    auth would expose the proxy (and messaging ``/stop``) to the network.
    """
    host = (settings.host or "").strip()
    if is_loopback_bind_host(host):
        return
    if settings.anthropic_auth_token.strip():
        return
    raise RuntimeError(
        "ANTHROPIC_AUTH_TOKEN is required when HOST is not loopback "
        f"(HOST={host!r}). Set a strong token, or bind to 127.0.0.1 for local-only use."
    )


def normalize_presented_api_token(presented: str, configured: str) -> str:
    """Normalize a client-presented API token for comparison.

    Some Claude-compatible clients append ``:model`` after the key. Only strip a
    colon suffix when the *configured* token itself has no colon, so tokens that
    legitimately contain ``:`` still work.
    """
    token = presented.strip()
    configured_token = configured.strip()
    if token and ":" in token and ":" not in configured_token:
        token = token.split(":", 1)[0].strip()
    return token
