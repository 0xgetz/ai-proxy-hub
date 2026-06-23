# AI Gateway

**AI Gateway (AIG)** is a middleware proxy that bridges the Claude Code CLI (Anthropic API) with multiple AI providers — including NVIDIA NIM, OpenRouter, Mistral, DeepSeek, Kimi, Wafer, OpenCode, Gemini, Fireworks, and more.

## Features

- 🔌 **Multi-provider support** — Route requests to NVIDIA NIM, OpenRouter, Mistral, DeepSeek, Kimi, Wafer, OpenCode, Gemini, Fireworks, and others
- 🎯 **Claude Code CLI integration** — Transparently proxies Anthropic API calls so Claude Code works with any supported backend
- 🛠️ **Codex support** — Also bridges OpenAI Codex CLI
- 📡 **Admin dashboard** — Web UI for configuration, monitoring, and messaging
- 💬 **Messaging integrations** — Telegram & Discord bot support
- 🎙️ **Voice support** — Optional NVIDIA Riva integration
- ⚡ **Streaming** — Full SSE streaming support with recovery
- 🔧 **Configurable** — Environment-based and admin-panel configuration

## Quick Start

### Prerequisites

- Python ≥ 3.14
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub

# Install with uv
uv sync

# Or with pip
pip install -e .
```

### Configuration

Copy the example env file and fill in your API keys:

```bash
cp .env.example .env
```

Key environment variables (see `.env.example` for the full list):

| Variable | Description |
|---|---|
| `NVIDIA_NIM_API_KEY` | NVIDIA NIM API key |
| `OPENROUTER_API_KEY` | OpenRouter API key |
| `MISTRAL_API_KEY` | Mistral La Plateforme API key |
| `DEEPSEEK_API_KEY` | DeepSeek API key |
| `KIMI_API_KEY` | Kimi (Moonshot) API key |
| `AIG_SMOKE_MODEL_*` | Smoke test model overrides |

### Running the Server

```bash
# Using the CLI entrypoint
aig-server

# Or directly
python server.py
```

### Launching Claude Code

```bash
aig-claude
```

### Launching Codex

```bash
aig-codex
```

### Initialize Configuration

```bash
aig-init
```

## CLI Commands

| Command | Description |
|---|---|
| `aig-server` | Start the gateway server |
| `aig-init` | Initialize configuration |
| `aig-claude` | Launch Claude Code through the gateway |
| `aig-codex` | Launch Codex through the gateway |
| `ai-gateway` | Alias for `aig-server` |

## Architecture

AI Gateway sits between the CLI client and the AI provider:

```
Claude Code CLI  →  AI Gateway (AIG)  →  AI Provider (NIM / OpenRouter / Mistral / ...)
```

The gateway translates Anthropic Messages API requests into provider-specific formats, streams responses back, and handles tool calls, thinking blocks, and error mapping.

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed design documentation.

## Project Structure

```
ai-gateway/
├── api/            # FastAPI server, routes, admin panel
├── cli/            # CLI entrypoints and launchers
├── config/         # Configuration, settings, paths
├── core/           # Core translation logic (Anthropic, OpenAI Responses)
├── providers/      # Provider-specific request/response handling
├── messaging/      # Telegram & Discord bot integrations
├── smoke/          # Smoke tests
├── tests/          # Unit & integration tests
├── scripts/        # Install/uninstall scripts
├── assets/         # Diagrams and screenshots
└── server.py       # Server entry point
```

## Development

```bash
# Run tests
uv run pytest

# Run smoke tests
uv run pytest smoke/
```

## License

This project is provided as-is. See repository for details.

---

**AI Gateway** — Bridging Claude Code with the world's AI providers.