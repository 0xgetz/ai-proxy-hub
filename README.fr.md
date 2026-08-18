<div align="center">

<img src="assets/logo.png" alt="AI Gateway Logo" width="200" height="200" />

# AI Gateway (AIG)

### Middleware proxy multi-fournisseur pour Claude Code CLI et Codex

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

AI Gateway (AIG) est un middleware proxy local qui relie Claude Code CLI et OpenAI Codex CLI à plusieurs fournisseurs d'IA, sans modifier le code de votre application.

### Pourquoi AI Gateway ?

| Besoin | Réponse d'AI Gateway |
|---|---|
| Les CLI utilisent des API différentes | Traduction transparente entre les protocoles Anthropic, OpenAI et les fournisseurs configurés |

---

## Fournisseurs pris en charge

AI Gateway prend en charge **17 fournisseurs** : 14 services cloud et 3 fournisseurs locaux.

### Fournisseurs cloud

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

### Fournisseurs locaux (sans clé API)

15. **LM Studio** (`lmstudio` — `http://localhost:1234/v1`)
16. **Llama.cpp** (`llamacpp` — `http://localhost:8080/v1`)
17. **Ollama** (`ollama` — `http://localhost:11434`)

---

## Installation rapide

```bash
git clone https://github.com/0xgetz/ai-proxy-hub.git
cd ai-proxy-hub
uv sync
cp .env.example .env
aig-server
```

## Commandes principales

| Command | Purpose |
|---|---|
| `aig-server` | Start the gateway server |
| `aig-init` | Initialize the configuration |
| `aig-claude` | Start Claude Code through the gateway |
| `aig-codex` | Start Codex through the gateway |
| `ai-gateway` | Alias for `aig-server` |

Pour les instructions de configuration, de sécurité et d'exploitation, consultez le [README principal](README.md) et [ARCHITECTURE.md](ARCHITECTURE.md).

---

## Licence

Distribué sous licence MIT. Consultez [LICENSE](LICENSE) pour plus d'informations.
