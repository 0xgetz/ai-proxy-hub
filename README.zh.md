<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# 🚀 AI Gateway (AIG)

### 适用于 Claude Code CLI 与 Codex 的多供应商代理中间件

**v2.4.0** · Python ≥ 3.14 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.4.0-orange)]()

[![EN](https://img.shields.io/badge/EN-English-1f6feb?style=flat-square)](README.en.md) [![ID](https://img.shields.io/badge/ID-Bahasa%20Indonesia-d9480f?style=flat-square)](README.id.md) [![ZH](https://img.shields.io/badge/ZH-中文-b91c1c?style=flat-square)](README.zh.md) [![ES](https://img.shields.io/badge/ES-Español-15803d?style=flat-square)](README.es.md) [![JA](https://img.shields.io/badge/JA-日本語-7c3aed?style=flat-square)](README.ja.md)
[![FR](https://img.shields.io/badge/FR-Français-2563eb?style=flat-square)](README.fr.md) [![DE](https://img.shields.io/badge/DE-Deutsch-1d4ed8?style=flat-square)](README.de.md) [![PT-BR](https://img.shields.io/badge/PT-BR-Português%20(Brasil)-047857?style=flat-square)](README.pt-BR.md) [![IT](https://img.shields.io/badge/IT-Italiano-166534?style=flat-square)](README.it.md) [![TR](https://img.shields.io/badge/TR-Türkçe-be123c?style=flat-square)](README.tr.md)
[![RU](https://img.shields.io/badge/RU-Русский-1e40af?style=flat-square)](README.ru.md) [![KO](https://img.shields.io/badge/KO-한국어-0f766e?style=flat-square)](README.ko.md) [![AR](https://img.shields.io/badge/AR-العربية-a16207?style=flat-square)](README.ar.md) [![HI](https://img.shields.io/badge/HI-हिन्दी-c2410c?style=flat-square)](README.hi.md) [![VI](https://img.shields.io/badge/VI-Tiếng%20Việt-0f766e?style=flat-square)](README.vi.md)

</div>

---

## 📖 关于 AI Gateway

**AI Gateway (AIG)** 是一个本地代理中间件，用于将 **Claude Code CLI** (Anthropic API) 和 **OpenAI Codex CLI** 连接到各种 AI 提供商，而无需修改您的应用程序代码。

网关接收来自 Claude Code 的 Anthropic Messages 格式和来自 Codex 的 OpenAI Responses 格式，将其转换为目标提供商（NVIDIA NIM、OpenRouter、Gemini、DeepSeek 等）理解的格式，并以完全相同的协议将响应流回 CLI。

---

## 🔌 支持的供应商

AI Gateway 支持 **17 个供应商**（14 个云端供应商和 3 个本地供应商：NVIDIA NIM、OpenRouter、Gemini、DeepSeek、Mistral、Codestral、Kimi、Wafer、Fireworks AI、Z.ai、OpenCode Zen、OpenCode Go、Groq、Cerebras、LM Studio、Llama.cpp、Ollama）。

---

## 🚀 快速安装

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
pip install -e .
```

详细信息请参见 [README.md](README.md)。

---

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE)。
