<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# 🚀 AI Gateway (AIG)

### Multi-Provider Proxy Middleware for Claude Code CLI & Codex

**v2.4.0** · Python ≥ 3.12 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.4.0-orange)]()

[English](README.en.md) | [Bahasa Indonesia](README.id.md) | [中文](README.zh.md) | [Español](README.es.md) | [日本語](README.ja.md)

</div>

---

## 📖 About AI Gateway

**AI Gateway (AIG)** is a local proxy middleware that bridges **Claude Code CLI** (Anthropic API) and **OpenAI Codex CLI** with a wide array of AI providers without requiring changes to your application code.

The gateway accepts Anthropic Messages format from Claude Code and OpenAI Responses format from Codex, translates them into the format understood by the target provider (NVIDIA NIM, OpenRouter, Gemini, DeepSeek, local models, etc.), and streams responses back to the CLI using the exact protocol expected.

### Why AI Gateway?

| Challenge | AI Gateway Solution |
|---|---|
| Claude Code only supports Anthropic API | 🔁 Route requests to any provider (NIM, Gemini, DeepSeek, etc.) |
| High Anthropic API costs | 💰 Utilize free or cost-effective alternative providers |
| Try different models without changing code | 🎛️ Switch providers seamlessly via environment variables or admin panel |
| Control via Telegram/Discord | 💬 Integrated messaging bots |
| Real-time monitoring & configuration | 📊 Web-based admin dashboard |

---

## 🔌 Supported Providers

AI Gateway supports **17 providers** — 14 cloud-based and 3 local:

### Cloud Providers
1. **NVIDIA NIM** (`nvidia_nim`)
2. **OpenRouter** (`open_router`)
3. **Gemini / Google** (`gemini`)
4. **DeepSeek** (`deepseek`)
5. **Mistral** (`mistral`)
6. **Codestral** (`mistral_codestral`)
7. **Kimi / Moonshot** (`kimi`)
8. **Wafer** (`wafer`)
9. **Fireworks AI** (`fireworks`)
10. **Z.ai** (`zai`)
11. **OpenCode Zen** (`opencode`)
12. **OpenCode Go** (`opencode_go`)
13. **Groq** (`groq`)
14. **Cerebras** (`cerebras`)

### Local Providers (No API Key Required)
15. **LM Studio** (`lmstudio` - `http://localhost:1234/v1`)
16. **Llama.cpp** (`llamacpp` - `http://localhost:8080/v1`)
17. **Ollama** (`ollama` - `http://localhost:11434`)

---

## 🚀 Quick Installation

```bash
# Clone repository
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub

# Install dependencies using uv or pip
pip install -e .
```

For detailed setup instructions, architecture documentation, and usage guides, please refer to [README.md](README.md) or [ARCHITECTURE.md](ARCHITECTURE.md).

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
