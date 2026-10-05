# API - Generative AI Foundations

The backend service for the Generative AI Foundations project. It provides a Python foundation for working with large language models (LLMs) through [LangChain](https://python.langchain.com/), using locally hosted models served by [Ollama](https://ollama.com/).

---

## Table of Contents

- [Overview](#overview)
- [Project Status](#project-status)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Configuration](#configuration)
- [Dependency Management](#dependency-management)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Author](#author)

---

## Overview

This service connects to a local LLM through the `langchain-ollama` integration. Because inference runs entirely on the local machine, it requires:

- no external API keys or paid model providers,
- no network calls to third-party inference services,
- no data leaving the machine.

The current entry point creates a `ChatOllama` client for the `gemma3:1b` model, sends a single prompt, and prints the model's reply. This is the minimal working baseline for the service.

---

## Project Status

The project is in early development. The table below shows what each component currently does.

| Component            | Status        | Notes                                                    |
| -------------------- | ------------- | -------------------------------------------------------- |
| LLM client (Ollama)  | Implemented   | `app/main.py` invokes `gemma3:1b` via `ChatOllama`.      |
| Dependency manifest  | Implemented   | `pyproject.toml`, `uv.lock`, and `requirements.txt`.     |
| Environment config   | Planned       | `.env.example` exists but has no variables defined yet.  |
| Containerization     | Planned       | `Dockerfile` and `.dockerignore` are placeholders.       |
| HTTP API layer       | Planned       | No web framework or endpoints are defined yet.           |

---

## Technology Stack

| Category             | Technology                                       |
| -------------------- | ------------------------------------------------ |
| Language             | Python 3.13                                      |
| LLM framework        | LangChain (`langchain-core`, `langchain-ollama`) |
| Model runtime        | Ollama                                           |
| Default model        | `gemma3:1b`                                      |
| Package manager      | [uv](https://docs.astral.sh/uv/)                 |

---

## Project Structure

```
api/
├── app/
│   ├── __init__.py        # Marks the app directory as a Python package
│   └── main.py            # Application entry point (LLM client and invocation)
├── .dockerignore          # Files excluded from the Docker build context
├── .env.example           # Template for environment variables
├── .gitignore             # Files excluded from version control
├── .python-version        # Pinned Python version (3.13) used by uv
├── Dockerfile             # Container image definition
├── pyproject.toml         # Project metadata and direct dependencies
├── requirements.txt       # Fully pinned dependency list for pip-based installs
├── uv.lock                # Reproducible lockfile managed by uv
└── README.md              # Project documentation
```

---

## Prerequisites

Make sure the following are installed before you set up the project:

1. **Python 3.13 or later.** The required version is pinned in `.python-version`.
2. **uv** (recommended), the Python package and project manager.

   ```bash
   # macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Or, using Homebrew
   brew install uv
   ```

3. **Ollama**, the local model runtime.

   ```bash
   # macOS, using Homebrew
   brew install ollama
   ```

   For other platforms, follow the instructions at [ollama.com/download](https://ollama.com/download).

---

## Getting Started

### 1. Clone the repository and change into the API directory

```bash
git clone <repository-url>
cd genai-foundations/api
```

### 2. Start the Ollama server

```bash
ollama serve
```

If you installed the Ollama desktop application, the server may already be running in the background. By default it listens on `http://localhost:11434`.

### 3. Download the model

```bash
ollama pull gemma3:1b
```

To confirm that the model is available:

```bash
ollama list
```

### 4. Install dependencies

**Option A: uv (recommended)**

```bash
uv sync
```

This creates a virtual environment in `.venv` and installs the exact versions recorded in `uv.lock`.

**Option B: pip**

```bash
python3.13 -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the Application

Run these commands from the `api/` directory.

**With uv:**

```bash
uv run python -m app.main
```

**With an activated virtual environment:**

```bash
python -m app.main
```

The script sends the prompt `"Hi"` to the model and prints the response to standard output. The exact output depends on the model, but it should look similar to this:

```
Hello! How can I help you today?
```

---

## Configuration

The model settings are currently defined directly in `app/main.py`:

| Parameter     | Current Value | Description                                                     |
| ------------- | ------------- | --------------------------------------------------------------- |
| `model`       | `gemma3:1b`   | The Ollama model used for inference.                            |
| `temperature` | `0.7`         | Controls randomness. Lower values give more deterministic output. |

To use a different model, pull it with Ollama first (for example, `ollama pull llama3.2`), then update the `model` argument in `app/main.py`.

Environment-based configuration through `.env` is planned. When it is added, copy the template and fill in the required values:

```bash
cp .env.example .env
```

Never commit the `.env` file to version control.

---

## Dependency Management

Direct dependencies are declared in `pyproject.toml`. The resolved dependency tree is locked in `uv.lock`.

**Add a new dependency:**

```bash
uv add <package-name>
```

**Remove a dependency:**

```bash
uv remove <package-name>
```

**Update `requirements.txt` after changing dependencies:**

```bash
uv pip freeze > requirements.txt
```

Commit `pyproject.toml`, `uv.lock` and `requirements.txt` together so that all installation methods stay consistent.

---

## Troubleshooting

| Symptom                                                   | Likely Cause                          | Resolution                                                    |
| --------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------- |
| `ConnectionError` or connection refused on port `11434`   | The Ollama server is not running.     | Start it with `ollama serve`, or open the Ollama application. |
| `model "gemma3:1b" not found`                             | The model has not been downloaded.    | Run `ollama pull gemma3:1b`.                                  |
| `ModuleNotFoundError: No module named 'langchain_ollama'` | Dependencies are not installed, or the virtual environment is not active. | Run `uv sync`, or activate `.venv` and reinstall the requirements. |
| Python version error during install                       | The interpreter is older than 3.13.   | Install Python 3.13, or let uv manage it with `uv python install 3.13`. |
| Slow responses                                            | Limited local hardware resources.     | Use a smaller model or close other resource-heavy applications. |

---

## Contributing

1. Create a feature branch from `main`.
2. Keep changes focused, and document any new configuration or dependencies in this README.
3. Make sure the application runs successfully before you open a pull request.
4. Write clear, descriptive commit messages.

---

## Author

**Rizwan**
