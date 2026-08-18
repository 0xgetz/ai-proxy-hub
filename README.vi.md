<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# AI Gateway (AIG)

### Phần mềm trung gian proxy đa nhà cung cấp cho Claude Code CLI và Codex

**v2.4.0** · Python ≥ 3.14 · FastAPI · OpenAI-Compatible

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

[![EN](https://img.shields.io/badge/EN-English-1f6feb?style=flat-square)](README.en.md) [![ID](https://img.shields.io/badge/ID-Bahasa%20Indonesia-d9480f?style=flat-square)](README.id.md) [![ZH](https://img.shields.io/badge/ZH-中文-b91c1c?style=flat-square)](README.zh.md) [![ES](https://img.shields.io/badge/ES-Español-15803d?style=flat-square)](README.es.md) [![JA](https://img.shields.io/badge/JA-日本語-7c3aed?style=flat-square)](README.ja.md)
[![FR](https://img.shields.io/badge/FR-Français-2563eb?style=flat-square)](README.fr.md) [![DE](https://img.shields.io/badge/DE-Deutsch-1d4ed8?style=flat-square)](README.de.md) [![PT-BR](https://img.shields.io/badge/PT-BR-Português%20(Brasil)-047857?style=flat-square)](README.pt-BR.md) [![IT](https://img.shields.io/badge/IT-Italiano-166534?style=flat-square)](README.it.md) [![TR](https://img.shields.io/badge/TR-Türkçe-be123c?style=flat-square)](README.tr.md)
[![RU](https://img.shields.io/badge/RU-Русский-1e40af?style=flat-square)](README.ru.md) [![KO](https://img.shields.io/badge/KO-한국어-0f766e?style=flat-square)](README.ko.md) [![AR](https://img.shields.io/badge/AR-العربية-a16207?style=flat-square)](README.ar.md) [![HI](https://img.shields.io/badge/HI-हिन्दी-c2410c?style=flat-square)](README.hi.md) [![VI](https://img.shields.io/badge/VI-Tiếng%20Việt-0f766e?style=flat-square)](README.vi.md)

</div>

---

## AI Gateway

AI Gateway (AIG) là phần mềm trung gian proxy cục bộ kết nối Claude Code CLI và OpenAI Codex CLI với nhiều nhà cung cấp AI mà không cần thay đổi mã ứng dụng.

### Vì sao dùng AI Gateway?

| Nhu cầu | Giải pháp AI Gateway |
|---|---|
| Các CLI dùng những API khác nhau | Chuyển đổi minh bạch giữa giao thức Anthropic, OpenAI và các nhà cung cấp đã cấu hình |

---

## Nhà cung cấp được hỗ trợ

AI Gateway hỗ trợ **17 nhà cung cấp**: 14 dịch vụ đám mây và 3 nhà cung cấp cục bộ.

### Nhà cung cấp đám mây

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

### Nhà cung cấp cục bộ (không cần khóa API)

15. **LM Studio** (`lmstudio` — `http://localhost:1234/v1`)
16. **Llama.cpp** (`llamacpp` — `http://localhost:8080/v1`)
17. **Ollama** (`ollama` — `http://localhost:11434`)

---

## Cài đặt nhanh

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
uv sync
cp .env.example .env
aig-server
```

## Lệnh chính

| Command | Purpose |
|---|---|
| `aig-server` | Start the gateway server |
| `aig-init` | Initialize the configuration |
| `aig-claude` | Start Claude Code through the gateway |
| `aig-codex` | Start Codex through the gateway |
| `ai-gateway` | Alias for `aig-server` |

Để biết hướng dẫn cấu hình, bảo mật và vận hành, hãy xem [README chính](README.md) và [ARCHITECTURE.md](ARCHITECTURE.md).

---

## Giấy phép

Phân phối theo giấy phép MIT. Xem [LICENSE](LICENSE) để biết thêm thông tin.
