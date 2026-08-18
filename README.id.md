<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# 🚀 AI Gateway (AIG)

### Proxy Middleware untuk Claude Code CLI & Codex dengan Dukungan Multi-Provider

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
