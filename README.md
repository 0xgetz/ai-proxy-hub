<div align="center">

# 🚀 AI Gateway (AIG)

### Proxy Middleware untuk Claude Code CLI & Codex dengan Dukungan Multi-Provider

**v2.4.0** · Python ≥ 3.14 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.4.0-orange)]()

</div>

---

## 📋 Daftar Isi

- [Tentang AI Gateway](#-tentang-ai-gateway)
- [Demo & Screenshot](#-demo--screenshot)
- [Arsitektur Sistem](#-arsitektur-sistem)
- [Provider yang Didukung](#-provider-yang-didukung)
- [Fitur Utama](#-fitur-utama)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Instalasi](#-instalasi)
- [Konfigurasi](#-konfigurasi)
- [Penggunaan](#-penggunaan)
- [Panel Admin Web](#-panel-admin-web)
- [Integrasi Messaging](#-integrasi-messaging-telegram--discord)
- [Dukungan Voice Note](#-dukungan-voice-note-transkripsi)
- [Pengujian](#-pengujian)
- [Struktur Proyek](#-struktur-proyek)
- [Pengembangan](#-pengembangan)
- [FAQ](#-faq-pertanyaan-yang-sering-diajukan)
- [Lisensi](#-lisensi)

---

## 📖 Tentang AI Gateway

**AI Gateway (AIG)** adalah proxy middleware lokal yang menjembatani **Claude Code CLI** (Anthropic API) dan **OpenAI Codex CLI** dengan berbagai provider AI — tanpa perlu mengubah kode aplikasi Anda.

Gateway menerima request berformat Anthropic Messages dari Claude Code dan OpenAI Responses dari Codex, lalu menerjemahkannya ke format yang dimengerti oleh provider tujuan (NVIDIA NIM, OpenRouter, Gemini, DeepSeek, dll), dan mengalirkan response kembali ke CLI dengan protokol yang sama persis.

### Mengapa AI Gateway?

| Masalah | Solusi AI Gateway |
|---|---|
| Claude Code hanya mendukung Anthropic API | 🔁 Rute ke provider mana pun (NIM, Gemini, DeepSeek, dll) |
| Biaya API Anthropic tinggi | 💰 Gunakan provider gratis/lebih murah |
| Ingin mencoba model berbeda tanpa ganti kode | 🎛️ Ganti provider via env var atau panel admin |
| Ingin kontrol via Telegram/Discord | 💬 Bot messaging terintegrasi |
| Ingin monitoring & konfigurasi visual | 📊 Panel admin web real-time |

---

## 🎬 Demo & Screenshot

### Demo Gateway — Server & Claude Code

![Demo AI Gateway](assets/demo-gateway.jpeg)

*Screenshot: Terminal menjalankan `aig-server` dan `aig-claude`, ditampilkan bersamaan dengan panel admin web yang menunjukkan status provider.*

### Diagram Arsitektur Sistem

![Arsitektur AI Gateway](assets/architecture-diagram.jpeg)

*Diagram alur: Claude Code CLI & Codex CLI → AI Gateway → Multiple AI Providers, dengan Admin UI dan Messaging Bots.*

### Screenshot Admin Panel

![Admin Panel - Providers](assets/admin-page.png)

*Panel admin web menampilkan konfigurasi provider, status koneksi, dan pengaturan model.*

### Screenshot Admin Messaging

![Admin Panel - Messaging](assets/admin-messaging.png)

*Konfigurasi integrasi messaging (Telegram/Discord) melalui panel admin.*

### Model Picker di Claude Code

![Claude Code Model Picker](assets/cc-model-picker.png)

*Pemilihan model di Claude Code CLI melalui gateway.*

### Model Picker di Codex

![Codex Model Picker](assets/codex-model-picker.png)

*Pemilihan model di Codex CLI melalui gateway.*

### Codex CLI via Gateway

![Codex CLI](assets/codex.png)

*Codex CLI berjalan melalui AI Gateway.*

### Tampilan Utama

![Tampilan Utama](assets/pic.png)

---

## 🏗️ Arsitektur Sistem

AI Gateway berdiri di antara CLI klien dan provider AI, menerjemahkan protokol secara transparan:

```
┌─────────────────────┐
│  Claude Code CLI     │
│  (Anthropic API)     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐     ┌──────────────────────┐
│   AI Gateway (AIG)  │────▶│  NVIDIA NIM          │
│   - FastAPI Server  │────▶│  OpenRouter          │
│   - Request Pipeline│────▶│  Gemini (Google)     │
│   - Provider Router │────▶│  DeepSeek            │
│   - SSE Streaming   │────▶│  Mistral / Codestral │
│   - Error Mapping   │────▶│  Kimi (Moonshot)     │
│   - Tool Handling   │────▶│  Wafer               │
│   - Thinking Blocks │────▶│  Fireworks AI        │
│                     │────▶│  Z.ai                │
└─────────┬───────────┘────▶│  OpenCode (Zen/Go)   │
          │                 │  Groq                │
          │                 │  Cerebras            │
          ▼                 │  LM Studio (lokal)   │
┌─────────────────────┐     │  Llama.cpp (lokal)   │
│  Codex CLI           │    │  Ollama (lokal)      │
│  (OpenAI Responses)  │    └──────────────────────┘
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│  Admin UI (Web)      │
│  Telegram/Discord    │
└─────────────────────┘
```

### Tiga Permukaan Runtime

1. **HTTP Proxy** — Route FastAPI menerima traffic Anthropic-compatible dan OpenAI Responses-compatible, plus endpoint health, model-listing, stop, dan admin.
2. **CLI Launchers** — Entrypoint wrapper yang menyiapkan environment Claude Code dan Codex agar menarget proxy lokal.
3. **Messaging Bridge** — Adapter Discord/Telegram opsional yang mengubah pesan chat menjadi sesi CLI terkelola.

> 📄 Untuk dokumentasi arsitektur lengkap, lihat [ARCHITECTURE.md](ARCHITECTURE.md).

---

## 🔌 Provider yang Didukung

AI Gateway mendukung **17 provider** — 14 cloud dan 3 lokal:

### Provider Cloud

| # | Provider | ID | Transport | API Key Env | Dapatkan Key |
|---|---|---|---|---|---|
| 1 | **NVIDIA NIM** | `nvidia_nim` | OpenAI Chat | `NVIDIA_NIM_API_KEY` | [build.nvidia.com](https://build.nvidia.com/settings/api-keys) |
| 2 | **OpenRouter** | `open_router` | Anthropic Messages | `OPENROUTER_API_KEY` | [openrouter.ai/keys](https://openrouter.ai/keys) |
| 3 | **Gemini (Google)** | `gemini` | OpenAI Chat | `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com/apikey) |
| 4 | **DeepSeek** | `deepseek` | Anthropic Messages | `DEEPSEEK_API_KEY` | [platform.deepseek.com](https://platform.deepseek.com/api_keys) |
| 5 | **Mistral** | `mistral` | OpenAI Chat | `MISTRAL_API_KEY` | [console.mistral.ai](https://console.mistral.ai/) |
| 6 | **Codestral** | `mistral_codestral` | OpenAI Chat | `CODESTRAL_API_KEY` | [console.mistral.ai](https://console.mistral.ai/) |
| 7 | **Kimi (Moonshot)** | `kimi` | Anthropic Messages | `KIMI_API_KEY` | [platform.moonshot.ai](https://platform.moonshot.ai/) |
| 8 | **Wafer** | `wafer` | Anthropic Messages | `WAFER_API_KEY` | [pass.wafer.ai](https://pass.wafer.ai/) |
| 9 | **Fireworks AI** | `fireworks` | Anthropic Messages | `FIREWORKS_API_KEY` | [fireworks.ai](https://fireworks.ai/) |
| 10 | **Z.ai** | `zai` | Anthropic Messages | `ZAI_API_KEY` | [z.ai](https://z.ai/) |
| 11 | **OpenCode Zen** | `opencode` | OpenAI Chat | `OPENCODE_API_KEY` | [opencode.ai](https://opencode.ai/auth) |
| 12 | **OpenCode Go** | `opencode_go` | OpenAI Chat | `OPENCODE_API_KEY` | [opencode.ai](https://opencode.ai/auth) |
| 13 | **Groq** | `groq` | OpenAI Chat | `GROQ_API_KEY` | [console.groq.com](https://console.groq.com/docs/openai) |
| 14 | **Cerebras** | `cerebras` | OpenAI Chat | `CEREBRAS_API_KEY` | [inference.cerebras.ai](https://inference-docs.cerebras.ai/resources/openai) |

### Provider Lokal (Tanpa API Key)

| # | Provider | ID | URL Default |
|---|---|---|---|
| 15 | **LM Studio** | `lmstudio` | `http://localhost:1234/v1` |
| 16 | **Llama.cpp** | `llamacpp` | `http://localhost:8080/v1` |
| 17 | **Ollama** | `ollama` | `http://localhost:11434` |

### Kapabilitas per Provider

| Kapabilitas | Simbol | Keterangan |
|---|---|---|
| `chat` | 💬 | Chat completion dasar |
| `streaming` | ⚡ | SSE streaming response |
| `tools` | 🔧 | Dukungan function/tool calling |
| `thinking` | 🧠 | Dukungan reasoning/thinking blocks |
| `rate_limit` | 🚦 | Rate limiting bawaan |
| `native_anthropic` | 📡 | Native Anthropic Messages API |

---

## ✨ Fitur Utama

- 🔌 **17 Provider** — NVIDIA NIM, OpenRouter, Gemini, DeepSeek, Mistral, Codestral, Kimi, Wafer, Fireworks, Z.ai, OpenCode, Groq, Cerebras, LM Studio, Llama.cpp, Ollama
- 🎯 **Dual CLI Support** — Claude Code CLI (Anthropic Messages) & Codex CLI (OpenAI Responses)
- 🛠️ **Tool Calling** — Dukungan penuh function calling / tool use untuk semua provider yang mendukung
- 🧠 **Thinking Blocks** — Dukungan reasoning/thinking blocks dengan toggle per-model
- ⚡ **SSE Streaming** — Streaming real-time dengan recovery session untuk koneksi terputus
- 🔄 **Error Mapping** — Pemetaan error antar protokol yang komprehensif
- 📡 **Panel Admin Web** — UI real-time untuk konfigurasi, monitoring, dan kontrol server
- 💬 **Messaging Bots** — Integrasi Telegram & Discord untuk kontrol via chat
- 🎙️ **Voice Note** — Transkripsi voice note via Whisper (CPU/CUDA) atau NVIDIA Riva
- 🌐 **Web Tools** — Penanganan lokal `web_search` dan `web_fetch` Anthropic
- 🔒 **Proxy Support** — Dukungan proxy HTTP & SOCKS5 per provider
- 🚦 **Rate Limiting** — Rate limiting bawaan dengan konfigurasi fleksibel
- 🔐 **Auth Token** — API key opsional untuk melindungi endpoint gateway
- 📊 **Structured Trace Logs** — Logging terstruktur dengan redaksi otomatis kredensial
- 🧪 **Smoke Tests** — Suite pengujian end-to-end untuk semua provider

---

## 💻 Persyaratan Sistem

| Komponen | Minimum | Rekomendasi |
|---|---|---|
| **Python** | 3.14+ | 3.14+ |
| **uv** | Terbaru | Terbaru ([install](https://docs.astral.sh/uv/)) |
| **OS** | Linux / macOS / Windows | Linux / macOS |
| **RAM** | 256 MB | 512 MB+ |
| **Claude Code CLI** | Opsional | Untuk fitur `aig-claude` |
| **Codex CLI** | Opsional | Untuk fitur `aig-codex` |

---

## 📦 Instalasi

### Metode 1: uv (Direkomendasikan)

```bash
# Clone repository
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub

# Install dependencies dengan uv
uv sync

# (Opsional) Install dukungan voice via NVIDIA Riva
uv sync --extra voice

# (Opsional) Install dukungan voice lokal Whisper
uv sync --extra voice_local
```

### Metode 2: pip

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub

pip install -e .

# (Opsional) Voice support
pip install -e ".[voice]"
```

### Metode 3: Jalankan langsung tanpa install

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub

uv run python server.py
```

---

## ⚙️ Konfigurasi

### Langkah 1: Salin file konfigurasi

```bash
cp .env.example .env
```

### Langkah 2: Isi API Key provider

Edit file `.env` dan isi API key untuk provider yang ingin Anda gunakan:

```bash
# Contoh: Isi minimal satu provider
NVIDIA_NIM_API_KEY="nvapi-xxxxxxxxxxxx"
OPENROUTER_API_KEY="sk-or-v1-xxxxxxxxxxxx"
GEMINI_API_KEY="AIzaSyxxxxxxxxxxxx"
DEEPSEEK_API_KEY="sk-xxxxxxxxxxxx"
```

> 💡 **Tip:** Anda tidak perlu mengisi semua provider. Cukup isi satu atau beberapa yang ingin Anda gunakan.

### Langkah 3: Pilih model default

Atur model default yang akan digunakan untuk request Claude:

```bash
# Format: provider_id/model/name
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"

# Atau gunakan provider lain:
# MODEL="open_router/anthropic/claude-3.5-sonnet"
# MODEL="gemini/google/gemini-2.0-flash"
# MODEL="deepseek/deepseek/deepseek-chat"
```

### Konfigurasi Model per Tier Claude

Claude Code mengirim request untuk tiga tier model (Opus, Sonnet, Haiku). Anda dapat memetakan masing-masing ke provider berbeda:

```bash
MODEL_OPUS="open_router/anthropic/claude-3.5-sonnet"     # Model untuk Opus
MODEL_SONNET="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"  # Model untuk Sonnet
MODEL_HAIKU="gemini/google/gemini-2.0-flash"              # Model untuk Haiku
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"      # Fallback default
```

### Konfigurasi Lengkap

<details>
<summary>📋 Daftar lengkap variabel environment (.env)</summary>

```bash
# ═══════════════════════════════════════════════════════
# API KEYS - Provider Cloud
# ═══════════════════════════════════════════════════════
NVIDIA_NIM_API_KEY=""
OPENROUTER_API_KEY=""
MISTRAL_API_KEY=""
CODESTRAL_API_KEY=""
DEEPSEEK_API_KEY=""
KIMI_API_KEY=""
WAFER_API_KEY=""
OPENCODE_API_KEY=""
ZAI_API_KEY=""
FIREWORKS_API_KEY=""
GEMINI_API_KEY=""
GROQ_API_KEY=""
CEREBRAS_API_KEY=""

# ═══════════════════════════════════════════════════════
# PROVIDER LOKAL (tanpa API key)
# ═══════════════════════════════════════════════════════
LM_STUDIO_BASE_URL="http://localhost:1234/v1"
LLAMACPP_BASE_URL="http://localhost:8080/v1"
OLLAMA_BASE_URL="http://localhost:11434"

# ═══════════════════════════════════════════════════════
# PEMILIHAN MODEL
# ═══════════════════════════════════════════════════════
MODEL_OPUS=
MODEL_SONNET=
MODEL_HAIKU=
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"

# ═══════════════════════════════════════════════════════
# THINKING / REASONING
# ═══════════════════════════════════════════════════════
ENABLE_OPUS_THINKING=
ENABLE_SONNET_THINKING=
ENABLE_HAIKU_THINKING=
ENABLE_MODEL_THINKING=true

# ═══════════════════════════════════════════════════════
# PROXY PER PROVIDER (http/socks5)
# ═══════════════════════════════════════════════════════
NVIDIA_NIM_PROXY=""
OPENROUTER_PROXY=""
MISTRAL_PROXY=""
# ... (lihat .env.example untuk semua provider)

# ═══════════════════════════════════════════════════════
# RATE LIMITING
# ═══════════════════════════════════════════════════════
PROVIDER_RATE_LIMIT=1
PROVIDER_RATE_WINDOW=3
PROVIDER_MAX_CONCURRENCY=5

# ═══════════════════════════════════════════════════════
# HTTP TIMEOUTS (detik)
# ═══════════════════════════════════════════════════════
HTTP_READ_TIMEOUT=300
HTTP_WRITE_TIMEOUT=60
HTTP_CONNECT_TIMEOUT=60

# ═══════════════════════════════════════════════════════
# SERVER
# ═══════════════════════════════════════════════════════
ANTHROPIC_AUTH_TOKEN="freecc"
AIG_OPEN_BROWSER=true

# ═══════════════════════════════════════════════════════
# MESSAGING
# ═══════════════════════════════════════════════════════
MESSAGING_PLATFORM="discord"  # "telegram" | "discord" | "none"
MESSAGING_RATE_LIMIT=1
MESSAGING_RATE_WINDOW=1

# ═══════════════════════════════════════════════════════
# VOICE NOTE TRANSCRIPTION
# ═══════════════════════════════════════════════════════
VOICE_NOTE_ENABLED=false
WHISPER_DEVICE="nvidia_nim"  # "cpu" | "cuda" | "nvidia_nim"
WHISPER_MODEL="openai/whisper-large-v3"
HF_TOKEN=""

# ═══════════════════════════════════════════════════════
# TELEGRAM
# ═══════════════════════════════════════════════════════
TELEGRAM_BOT_TOKEN=""
ALLOWED_TELEGRAM_USER_ID=""

# ═══════════════════════════════════════════════════════
# DISCORD
# ═══════════════════════════════════════════════════════
DISCORD_BOT_TOKEN=""
ALLOWED_DISCORD_CHANNELS=""

# ═══════════════════════════════════════════════════════
# AGENT CONFIG
# ═══════════════════════════════════════════════════════
ALLOWED_DIR=""
FAST_PREFIX_DETECTION=true
ENABLE_NETWORK_PROBE_MOCK=true
ENABLE_TITLE_GENERATION_SKIP=true
ENABLE_SUGGESTION_MODE_SKIP=true
ENABLE_FILEPATH_EXTRACTION_MOCK=true

# ═══════════════════════════════════════════════════════
# WEB TOOLS
# ═══════════════════════════════════════════════════════
ENABLE_WEB_SERVER_TOOLS=true
WEB_FETCH_ALLOWED_SCHEMES=http,https
WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false

# ═══════════════════════════════════════════════════════
# LOGGING & DEBUG
# ═══════════════════════════════════════════════════════
DEBUG_PLATFORM_EDITS=false
DEBUG_SUBAGENT_STACK=false
LOG_RAW_API_PAYLOADS=false
LOG_RAW_SSE_EVENTS=false
LOG_API_ERROR_TRACEBACKS=false
LOG_RAW_MESSAGING_CONTENT=false
LOG_RAW_CLI_DIAGNOSTICS=false
LOG_MESSAGING_ERROR_DETAILS=false
```

</details>

---

## 🚀 Penggunaan

### 1. Jalankan Server Gateway

```bash
# Menggunakan CLI entrypoint
aig-server

# Atau langsung via Python
uv run python server.py

# Atau via uvicorn
uv run uvicorn server:app --host 0.0.0.0 --port 8082 --timeout-graceful-shutdown 5
```

Server akan mulai di `http://localhost:8082` dan panel admin otomatis terbuka di browser (jika `AIG_OPEN_BROWSER=true`).

### 2. Jalankan Claude Code melalui Gateway

```bash
aig-claude
```

Perintah ini akan:
- Menyiapkan environment variable agar Claude Code menarget proxy lokal
- Meluncurkan Claude Code CLI
- Semua request akan dirutekan melalui AI Gateway ke provider yang dikonfigurasi

### 3. Jalankan Codex melalui Gateway

```bash
aig-codex
```

### 4. Inisialisasi Konfigurasi

```bash
aig-init
```

Membuat file `.env` dari template dan memandu konfigurasi awal.

### Daftar Perintah CLI

| Perintah | Deskripsi |
|---|---|
| `aig-server` | Jalankan server gateway |
| `aig-init` | Inisialisasi konfigurasi awal |
| `aig-claude` | Launch Claude Code CLI melalui gateway |
| `aig-codex` | Launch Codex CLI melalui gateway |
| `ai-gateway` | Alias untuk `aig-server` |

### Contoh Alur Kerja Lengkap

```bash
# 1. Clone & install
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
uv sync

# 2. Konfigurasi
cp .env.example .env
# Edit .env, isi NVIDIA_NIM_API_KEY dan set MODEL

# 3. Jalankan server (di terminal 1)
aig-server

# 4. Jalankan Claude Code (di terminal 2)
aig-claude

# 5. Mulai coding! Claude Code akan menggunakan provider yang Anda konfigurasi
```

---

## 🖥️ Panel Admin Web

AI Gateway dilengkapi panel admin web yang dapat diakses di:

```
http://localhost:8082/admin
```

### Fitur Panel Admin

| Bagian | Fungsi |
|---|---|
| **Providers** | Lihat status & konfigurasi semua provider |
| **Model Config** | Atur pemetaan model per tier (Opus/Sonnet/Haiku) |
| **Messaging** | Konfigurasi bot Telegram/Discord |
| **Server Control** | Start/stop/restart server |
| **Logs** | Lihat log real-time |

![Admin Panel](assets/admin-page.png)

Panel admin memungkinkan Anda mengubah konfigurasi tanpa restart server — perubahan langsung diterapkan.

---

## 💬 Integrasi Messaging (Telegram & Discord)

AI Gateway mendukung kontrol via bot messaging — kirim perintah chat untuk menjalankan sesi Claude Code terkelola.

### Setup Telegram

1. Buat bot via [@BotFather](https://t.me/botfather) di Telegram
2. Dapatkan bot token dan user ID Anda
3. Isi di `.env`:

```bash
MESSAGING_PLATFORM="telegram"
TELEGRAM_BOT_TOKEN="123456:ABC-DEF..."
ALLOWED_TELEGRAM_USER_ID="123456789"
```

### Setup Discord

1. Buat bot di [Discord Developer Portal](https://discord.com/developers/applications)
2. Dapatkan bot token dan ID channel yang diizinkan
3. Isi di `.env`:

```bash
MESSAGING_PLATFORM="discord"
DISCORD_BOT_TOKEN="MTk2N..."
ALLOWED_DISCORD_CHANNELS="123456789012345678"
```

![Admin Messaging](assets/admin-messaging.png)

### Perintah via Chat

Setelah bot aktif, kirim pesan ke bot untuk berinteraksi dengan Claude Code:

- Kirim teks biasa → Claude Code akan memproses dan membalas
- Kirim voice note → Ditranskripsi lalu diproses (jika voice diaktifkan)
- Bot menjalankan sesi CLI terkelola dengan rate limiting

---

## 🎙️ Dukungan Voice Note (Transkripsi)

AI Gateway dapat mentranskripsi voice note dari pesan messaging:

### Opsi 1: NVIDIA Riva (Cloud)

```bash
VOICE_NOTE_ENABLED=true
WHISPER_DEVICE="nvidia_nim"
WHISPER_MODEL="openai/whisper-large-v3"
# Memerlukan NVIDIA_NIM_API_KEY
uv sync --extra voice
```

### Opsi 2: Whisper Lokal (CPU/CUDA)

```bash
VOICE_NOTE_ENABLED=true
WHISPER_DEVICE="cpu"  # atau "cuda" untuk GPU
WHISPER_MODEL="large-v3"  # pilihan: tiny, base, small, medium, large-v2, large-v3, large-v3-turbo
uv sync --extra voice_local
```

---

## 🧪 Pengujian

### Unit Tests

```bash
# Jalankan semua test
uv run pytest

# Jalankan test spesifik
uv run pytest tests/api/
uv run pytest tests/providers/
uv run pytest tests/cli/
```

### Smoke Tests (End-to-End)

Smoke test menguji integrasi penuh dengan provider sungguhan:

```bash
# Jalankan semua smoke test
uv run pytest smoke/

# Smoke test per provider
uv run pytest smoke/product/test_provider_product_live.py

# Smoke test CLI
uv run pytest smoke/product/test_cli_package_product_live.py
```

### Contract Tests

```bash
# Verifikasi arsitektur dan batasan import
uv run pytest tests/contracts/
```

### CI/CD

Proyek dilengkapi GitHub Actions workflow (`.github/workflows/tests.yml`) yang menjalankan test otomatis pada setiap push dan pull request.

---

## 📁 Struktur Proyek

```
ai-gateway/
├── api/                    # Server FastAPI & endpoint
│   ├── admin_static/       # Panel admin web (HTML/CSS/JS)
│   ├── models/             # Model Anthropic & OpenAI Responses
│   ├── web_tools/          # Penanganan web_search & web_fetch
│   ├── app.py              # Factory aplikasi FastAPI
│   ├── routes.py           # Route API utama
│   ├── request_pipeline.py # Pipeline pemrosesan request
│   ├── model_router.py     # Router pemilihan model
│   └── ...
├── cli/                    # CLI entrypoints & launchers
│   ├── entrypoints.py      # aig-server, aig-init
│   ├── launchers/          # aig-claude, aig-codex
│   ├── managed/            # Sesi CLI terkelola (untuk messaging)
│   └── ...
├── config/                 # Konfigurasi & settings
│   ├── settings.py         # Pydantic Settings (env-based)
│   ├── provider_catalog.py # Katalog metadata provider
│   ├── constants.py        # Konstanta HTTP & timeout
│   └── ...
├── core/                   # Logika translasi inti
│   ├── anthropic/          # Translasi Anthropic Messages
│   ├── openai_responses/   # Translasi OpenAI Responses
│   └── ...
├── providers/              # Handler per provider
│   ├── nvidia_nim/         # NVIDIA NIM
│   ├── open_router/        # OpenRouter
│   ├── gemini/             # Gemini
│   ├── deepseek/           # DeepSeek
│   ├── ...                 # Provider lainnya
│   ├── registry.py         # Registry provider
│   ├── error_mapping.py    # Pemetaan error antar protokol
│   └── rate_limit.py       # Rate limiting
├── messaging/              # Integrasi messaging
│   ├── telegram/           # Bot Telegram
│   ├── discord/            # Bot Discord
│   └── ...
├── smoke/                  # Smoke tests (E2E)
├── tests/                  # Unit & integration tests
├── scripts/               # Script install/uninstall
├── assets/                # Screenshot & diagram
├── server.py              # Entry point server
├── pyproject.toml         # Konfigurasi proyek & dependencies
├── .env.example           # Template konfigurasi
├── ARCHITECTURE.md        # Dokumentasi arsitektur
├── AGENTS.md              # Panduan untuk AI agents
├── CLAUDE.md              # Panduan khusus Claude Code
└── README.md              # File ini
```

---

## 🛠️ Pengembangan

### Setup Lingkungan Pengembangan

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
uv sync
uv run pytest  # Pastikan semua test lulus
```

### Menambahkan Provider Baru

1. Buat direktori di `providers/<nama_provider>/`
2. Implementasikan handler request/response
3. Daftarkan di `config/provider_catalog.py`
4. Tambahkan API key env di `.env.example`
5. Tulis smoke test di `smoke/product/`
6. Bump versi di `pyproject.toml`

### Versioning

Proyek menggunakan [Semantic Versioning](https://semver.org/). Setiap commit di `main` yang mengubah file produksi harus menyertakan bump versi di `pyproject.toml`.

File produksi: `api/`, `cli/`, `config/`, `core/`, `messaging/`, `providers/`, `.env.example`

### Menjalankan CI Lokal

```bash
# Linux/macOS
./scripts/ci.sh

# Windows
.\scripts\ci.ps1
```

---

## ❓ FAQ (Pertanyaan yang Sering Diajukan)

<details>
<summary><b>Apakah AI Gateway gratis?</b></summary>

Ya, AI Gateway adalah software open-source. Namun, provider AI yang Anda gunakan (NVIDIA NIM, OpenRouter, dll) mungkin memiliki biaya sendiri. Beberapa provider seperti LM Studio, Llama.cpp, dan Ollama berjalan lokal dan gratis.
</details>

<details>
<summary><b>Apakah saya perlu menginstall Claude Code CLI?</b></summary>

Hanya jika Anda ingin menggunakan fitur `aig-claude`. Gateway itu sendiri berjalan independen dan dapat melayani klien HTTP apa pun yang kompatibel dengan Anthropic API.
</details>

<details>
<summary><b>Bisakah saya menggunakan beberapa provider sekaligus?</b></summary>

Ya! Anda dapat mengisi API key untuk multiple provider dan memetakan model Claude yang berbeda (Opus, Sonnet, Haiku) ke provider yang berbeda menggunakan `MODEL_OPUS`, `MODEL_SONNET`, `MODEL_HAIKU`.
</details>

<details>
<summary><b>Bagaimana cara beralih provider tanpa restart?</b></summary>

Buka panel admin di `http://localhost:8082/admin`, ubah konfigurasi provider, dan perubahan akan langsung diterapkan tanpa restart server.
</details>

<details>
<summary><b>Apakah data saya aman?</b></summary>

AI Gateway berjalan lokal di mesin Anda. Request diteruskan langsung ke provider tanpa perantara. Log dengan redaksi otomatis kredensial. Namun, data yang dikirim ke provider AI tetap tunduk pada kebijakan privasi masing-masing provider.
</details>

<details>
<summary><b>Apakah mendukung streaming?</b></summary>

Ya, AI Gateway mendukung SSE (Server-Sent Events) streaming penuh dengan recovery session untuk koneksi yang terputus. Semua provider yang mendukung streaming akan otomatis menggunakan mode streaming.
</details>

<details>
<summary><b>Bisakah saya menggunakan proxy?</b></summary>

Ya, setiap provider mendukung konfigurasi proxy HTTP dan SOCKS5 secara independen. Contoh: `NVIDIA_NIM_PROXY="http://user:pass@host:port"` atau `OPENROUTER_PROXY="socks5://host:port"`.
</details>

---

## 📄 Lisensi

Proyek ini disediakan apa adanya (as-is). Lihat repository untuk detail.

---

<div align="center">

**AI Gateway (AIG)** — Menjembatani Claude Code dengan AI Provider dunia.

Dibuat dengan ❤️ oleh [0xgetz](https://github.com/0xgetz)

[⬆ Kembali ke atas](#-ai-gateway-aig)

</div>