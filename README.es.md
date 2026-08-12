<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# 🚀 AI Gateway (AIG)

### Middleware de Proxy Multiproveedor para Claude Code CLI y Codex

**v2.4.0** · Python ≥ 3.12 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.4.0-orange)]()

[English](README.en.md) | [Bahasa Indonesia](README.id.md) | [中文](README.zh.md) | [Español](README.es.md) | [日本語](README.ja.md)

</div>

---

## 📖 Sobre AI Gateway

**AI Gateway (AIG)** es un middleware de proxy local que conecta **Claude Code CLI** (Anthropic API) y **OpenAI Codex CLI** con múltiples proveedores de IA sin necesidad de cambiar el código de su aplicación.

El gateway acepta el formato de mensajes de Anthropic y las respuestas de OpenAI, traduciéndolas al formato compatible con el proveedor de destino (NVIDIA NIM, OpenRouter, Gemini, DeepSeek, etc.) y transmitiendo la respuesta de vuelta al CLI.

---

## 🔌 Proveedores Soportados

AI Gateway soporta **17 proveedores** (14 en la nube y 3 locales: NVIDIA NIM, OpenRouter, Gemini, DeepSeek, Mistral, Codestral, Kimi, Wafer, Fireworks AI, Z.ai, OpenCode Zen, OpenCode Go, Groq, Cerebras, LM Studio, Llama.cpp, Ollama).

---

## 🚀 Instalación Rápida

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
pip install -e .
```

Consulte [README.md](README.md) para más detalles.

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulte [LICENSE](LICENSE) para más información.
