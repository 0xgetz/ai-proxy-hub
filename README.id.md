<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# 🚀 AI Gateway (AIG)

### Proxy Middleware untuk Claude Code CLI & Codex dengan Dukungan Multi-Provider

**v2.4.0** · Python ≥ 3.14 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.4.0-orange)]()

[English](README.en.md) | [Bahasa Indonesia](README.id.md) | [中文](README.zh.md) | [Español](README.es.md) | [日本語](README.ja.md)

</div>

---

## 📖 Tentang AI Gateway

**AI Gateway (AIG)** adalah proxy middleware lokal yang menjembatani **Claude Code CLI** (Anthropic API) dan **OpenAI Codex CLI** dengan berbagai provider AI — tanpa perlu mengubah kode aplikasi Anda.

Gateway menerima request berformat Anthropic Messages dari Claude Code dan OpenAI Responses dari Codex, lalu menerjemahkannya ke format yang dimengerti oleh provider tujuan (NVIDIA NIM, OpenRouter, Gemini, DeepSeek, dll), dan mengalirkan response kembali ke CLI dengan protokol yang sama persis.

---

## 🔌 Provider yang Didukung

AI Gateway mendukung **17 provider** — 14 cloud dan 3 lokal (NVIDIA NIM, OpenRouter, Gemini, DeepSeek, Mistral, Codestral, Kimi, Wafer, Fireworks AI, Z.ai, OpenCode Zen, OpenCode Go, Groq, Cerebras, LM Studio, Llama.cpp, Ollama).

---

## 🚀 Instalasi Cepat

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
pip install -e .
```

Untuk panduan lengkap, lihat [README.md](README.md).

---

## 📄 Lisensi

Distribusi di bawah Lisensi MIT. Lihat [LICENSE](LICENSE) untuk detail.
