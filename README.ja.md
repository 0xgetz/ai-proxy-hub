<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# 🚀 AI Gateway (AIG)

### Claude Code CLI & Codex 向けマルチプロバイダープロキシミドルウェア

**v2.4.0** · Python ≥ 3.14 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.4.0-orange)]()

[English](README.en.md) | [Bahasa Indonesia](README.id.md) | [中文](README.zh.md) | [Español](README.es.md) | [日本語](README.ja.md)

</div>

---

## 📖 AI Gateway について

**AI Gateway (AIG)** は、アプリケーションコードを変更することなく、**Claude Code CLI** (Anthropic API) および **OpenAI Codex CLI** を多様な AI プロバイダーに接続するローカルプロキシミドルウェアです。

Claude Code からの Anthropic Messages 形式や Codex からの OpenAI Responses 形式を受け取り、ターゲットプロバイダー (NVIDIA NIM、OpenRouter、Gemini、DeepSeek など) が理解できる形式に変換してストリーミング返送します。

---

## 🔌 対応プロバイダー

AI Gateway は **17 のプロバイダー**（クラウド 14 社、ローカル 3 社：NVIDIA NIM、OpenRouter、Gemini、DeepSeek、Mistral、Codestral、Kimi、Wafer、Fireworks AI、Z.ai、OpenCode Zen、OpenCode Go、Groq、Cerebras、LM Studio、Llama.cpp、Ollama）をサポートしています。

---

## 🚀 クイックインストール

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
pip install -e .
```

詳細については [README.md](README.md) をご覧ください。

---

## 📄 ライセンス

MIT ライセンスの下で配布されています。[LICENSE](LICENSE) をご覧ください。
