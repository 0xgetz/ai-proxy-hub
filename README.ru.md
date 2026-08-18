<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# AI Gateway (AIG)

### Мультипровайдерное прокси-промежуточное ПО для Claude Code CLI и Codex

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

AI Gateway (AIG) — это локальное прокси-промежуточное ПО, которое подключает Claude Code CLI и OpenAI Codex CLI к нескольким поставщикам ИИ без изменения кода приложения.

### Зачем нужен AI Gateway?

| Задача | Решение AI Gateway |
|---|---|
| CLI используют разные API | Прозрачный перевод между протоколами Anthropic, OpenAI и настроенных поставщиков |

---

## Поддерживаемые поставщики

AI Gateway поддерживает **17 поставщиков**: 14 облачных сервисов и 3 локальных поставщика.

### Облачные поставщики

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

### Локальные поставщики (без ключа API)

15. **LM Studio** (`lmstudio` — `http://localhost:1234/v1`)
16. **Llama.cpp** (`llamacpp` — `http://localhost:8080/v1`)
17. **Ollama** (`ollama` — `http://localhost:11434`)

---

## Быстрая установка

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
uv sync
cp .env.example .env
aig-server
```

## Основные команды

| Command | Purpose |
|---|---|
| `aig-server` | Start the gateway server |
| `aig-init` | Initialize the configuration |
| `aig-claude` | Start Claude Code through the gateway |
| `aig-codex` | Start Codex through the gateway |
| `ai-gateway` | Alias for `aig-server` |

Инструкции по настройке, безопасности и эксплуатации доступны в [основном README](README.md) и [ARCHITECTURE.md](ARCHITECTURE.md).

---

## Лицензия

Распространяется по лицензии MIT. Подробности см. в [LICENSE](LICENSE).
