# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The repository holds a course, Generative AI Foundations, with 10 modules (the roadmap is in `docs/01-intro-to-genai/1.1-introduction-to-generative-ai.md`, Section 7). The Markdown lessons in `docs/` are the source of truth. `code/`, `notebooks/` and `api/` hold the runnable code that goes with them. Modules 1 and 2 are written. `docs/03-prompt-eng/` exists but is empty.

## How the pieces relate

- **`docs/NN-module-slug/N.N-lesson-slug.md`**: each lesson walks the learner through building scripts step by step ("Create `x.py`:", then `uv run x.py`). Every script a lesson creates belongs in the flat `code/` directory. Check-in lessons (`1.4`, `2.5`) list every script from their module and its expected output, so treat them as the acceptance checklist for `code/`.
- **`code/`**: the learner's project (`uv init code --python 3.13` in Lesson 1.2). It grows lesson by lesson:
  - `main.py` (Lesson 1.2) uses the native `ollama` SDK directly.
  - `llm.py` (Lesson 1.3) is the shared provider module. It holds a `PROVIDERS` dict (ollama, openai, gemini) and `get_client()`, which returns an `(OpenAI client, model)` tuple. All three providers go through the `openai` SDK using OpenAI-compatible `base_url`s, and the active provider is chosen by `PROVIDER` in `.env`. Later scripts (`chat.py`, `stream.py`, `structured.py`, and the Module 2 scripts such as `token_usage.py` and `openai_*.py`) import `get_client()` instead of hard-coding a model or key. Keep this pattern: adding a provider should only touch `llm.py`.
  - The LangChain scripts (`langchain_tokens.py`, `lc_*.py`, `memory_langgraph.py`) come in during Module 2.
  - Currently only `main.py` is implemented. `llm.py`, `chat.py`, `stream.py` and `structured.py` are empty placeholders whose intended code is in Lesson 1.3.
- **`notebooks/NN-module-slug/N.N-lesson-slug.ipynb`**: these mirror the lesson file names and run on the `code` project's virtual environment as their Jupyter kernel (`ipykernel` is a `code` dependency).
- **`api/`**: a separate uv project using `langchain-ollama` (`ChatOllama`). `app/main.py` is currently a single script with no HTTP framework. The `Dockerfile`, `api/.env.example` and the root `docker-compose.yml` are empty placeholders.

When you change code that a lesson shows, keep the lesson and the code in sync.

## Commands

`code/` and `api/` are independent uv projects (Python 3.13). Run commands from inside each one.

```bash
ollama serve                      # local model server, http://localhost:11434
ollama pull gemma3:1b             # default model used by code/main.py and api/app/main.py

cd code && uv sync && uv run main.py          # any lesson script: uv run <script>.py
cd api  && uv sync && uv run python -m app.main
uv add <pkg>                                  # updates pyproject.toml and uv.lock
uv pip freeze > requirements.txt              # api/ only: keep requirements.txt in sync after dependency changes
```

No test suite, linter or formatter is configured. To verify a script, run it against a running Ollama server and compare its output with the "Expected result" column in the module's check-in lesson.

## Known inconsistencies

- **Model name:** the lessons (1.3, 1.4) use `gemma4:e2b` as the Ollama model, but `code/main.py`, `api/app/main.py` and the READMEs use `gemma3:1b`. Ask which one to standardize on before changing either.
- **Missing dependencies:** lessons expect `code/` to contain `openai`, `python-dotenv`, `pydantic`, `tiktoken`, LangChain and LangGraph packages, and a `.env` file with `PROVIDER=ollama`. So far its `pyproject.toml` only declares `ollama` and `ipykernel`. Add packages with `uv add` when implementing the lesson that introduces them.

## Lesson writing conventions

Follow the existing lessons exactly when adding or editing them:

- **Header block:** `# Generative AI Foundations`, then `## Module N: Title`, an optional italic subtitle, then `### N.N Lesson Title`, separated from the body by `---`.
- **Body sections:** numbered `## 1. ...` sections separated by `---`. Each concept opens with a bold one-sentence definition, followed by a `> **Mental Model: Name**` blockquote analogy. Use tables for comparisons and timelines.
- **Code sections:** a Setup section (`uv add ...`), then numbered scripts, each followed by a line-by-line explanation table and its expected output.
- **Ending:** close with `## Key Takeaways`, a `**Practice:**` task, and the italic footer `*Generative AI Foundations · Module N · Lesson N.N*`.
- **Check-ins:** use Parts A to D (Lab/Setup Checklist, Concept Check, Code Check, Mini Challenge), with answers at the end.
- **Style:** plain, simple English for beginners. Examples use Pakistani context (names such as Ali and Sara, cities such as Lahore). The content is dated to 2026. Do not use emojis in docs or READMEs.
