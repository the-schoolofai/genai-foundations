# Code - Generative AI Foundations

Practical Python examples for working with large language models (LLMs) through the official [Ollama Python library](https://github.com/ollama/ollama-python). Each script shows one core generative AI concept, such as system prompts, chat messages and streaming. The examples run on local models, and can optionally use Ollama cloud models.

---

## Table of Contents

- [Overview](#overview)
- [Project Status](#project-status)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running the Examples](#running-the-examples)
- [Configuration](#configuration)
- [Using Cloud Models](#using-cloud-models)
- [Working with Jupyter](#working-with-jupyter)
- [Dependency Management](#dependency-management)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Author](#author)

---

## Overview

This project is a hands-on companion to the Generative AI Foundations material. It uses the Ollama client library directly, without a higher-level framework, so you can see exactly how messages are structured, sent to a model and returned.

The main example, `main.py`, sets up a customer support assistant for an online store. It:

1. defines a **system prompt** that sets the assistant's role, tone and response length,
2. builds a **message list** with `system` and `user` roles,
3. sends the conversation to the model with **streaming** enabled,
4. prints each part of the response as soon as it arrives.

---

## Project Status

The project is in early development. The table below shows what each module currently does.

| File              | Status      | Purpose                                                                |
| ----------------- | ----------- | ---------------------------------------------------------------------- |
| `main.py`         | Implemented | Customer support assistant with a system prompt and streamed output.   |
| `llm.py`          | Planned     | Shared provider module: `get_client()` selects Ollama, OpenAI or Gemini from `.env` (Lesson 1.3). |
| `chat.py`         | Planned     | First Chat Completions call through `llm.py` (Lesson 1.3).             |
| `stream.py`       | Planned     | Streaming with the OpenAI SDK through `llm.py` (Lesson 1.3).           |
| `structured.py`   | Planned     | Structured output parsed into a Pydantic model (Lesson 1.3).           |
| `.env.example`    | Planned     | Template for environment-based configuration.                          |

---

## Technology Stack

| Category          | Technology                                         |
| ----------------- | -------------------------------------------------- |
| Language          | Python 3.13                                        |
| LLM client        | `ollama` (official Ollama Python library)          |
| Model runtime     | Ollama (local), with optional Ollama cloud models  |
| Default model     | `gemma3:1b`                                        |
| Notebook support  | `ipykernel`                                        |
| Package manager   | [uv](https://docs.astral.sh/uv/)                   |

---

## Project Structure

```
code/
├── main.py            # Customer support assistant with streamed responses
├── llm.py             # Shared provider module and get_client() (planned)
├── chat.py            # First Chat Completions call (planned)
├── stream.py          # Streaming with the OpenAI SDK (planned)
├── structured.py      # Structured output with Pydantic (planned)
├── .env.example       # Template for environment variables
├── .gitignore         # Files excluded from version control
├── .python-version    # Pinned Python version (3.13) used by uv
├── pyproject.toml     # Project metadata and dependencies
├── uv.lock            # Reproducible lockfile managed by uv
└── README.md          # Project documentation
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

### 1. Clone the repository and change into the code directory

```bash
git clone <repository-url>
cd genai-foundations/code
```

### 2. Start the Ollama server

```bash
ollama serve
```

If you installed the Ollama desktop application, the server may already be running in the background. By default it listens on `http://localhost:11434`.

### 3. Download the default model

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
pip install ollama ipykernel
```

---

## Running the Examples

Run these commands from the `code/` directory.

**With uv:**

```bash
uv run main.py
```

**With an activated virtual environment:**

```bash
python main.py
```

The script asks the support assistant:

```
My order arrived damaged. What should I do?
```

The response appears on the terminal word by word as the model generates it. The exact wording depends on the model, but it should be a polite reply with clear next steps, under 80 words.

To ask a different question, change the argument passed to `ask_support()` at the bottom of `main.py`.

---

## Configuration

The settings are currently defined as constants at the top of `main.py`:

| Constant        | Current Value                                       | Description                                                  |
| --------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| `MODEL`         | `gemma3:1b`                                         | The Ollama model used for inference.                         |
| `SYSTEM_PROMPT` | Customer support assistant for an online store      | Sets the assistant's role, tone and maximum response length. |

To try a different local model, pull it first (for example, `ollama pull llama3.2`), then update `MODEL`.

Environment-based configuration through `.env` is planned. When it is added, copy the template and fill in the required values:

```bash
cp .env.example .env
```

Never commit the `.env` file to version control.

---

## Using Cloud Models

Ollama can run larger models on its cloud infrastructure instead of your machine. This is useful when a model is too large for your local hardware.

1. Sign in to your Ollama account:

   ```bash
   ollama signin
   ```

2. Change the model in `main.py`:

   ```python
   MODEL = "gemma4:31b-cloud"
   ```

3. Run the example as usual. The application code stays the same, because requests still go through the local Ollama server, which forwards them to the cloud.

Unlike local models, cloud models send prompts to Ollama's servers. Do not use them with sensitive data unless that is acceptable for your use case.

---

## Working with Jupyter

The project includes `ipykernel`, so you can use its virtual environment as a Jupyter kernel for interactive experiments, such as the notebooks in this repository.

```bash
uv run python -m ipykernel install --user --name genai-code --display-name "GenAI Code (Python 3.13)"
```

After you register the kernel, select **GenAI Code (Python 3.13)** in Jupyter or VS Code.

---

## Dependency Management

Dependencies are declared in `pyproject.toml`. The resolved dependency tree is locked in `uv.lock`.

**Add a new dependency:**

```bash
uv add <package-name>
```

**Remove a dependency:**

```bash
uv remove <package-name>
```

Commit `pyproject.toml` and `uv.lock` together so that every environment installs the same versions.

---

## Troubleshooting

| Symptom                                                  | Likely Cause                                   | Resolution                                                           |
| -------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------- |
| `ConnectionError` or connection refused on port `11434`  | The Ollama server is not running.              | Start it with `ollama serve`, or open the Ollama application.        |
| `model "gemma3:1b" not found`                            | The model has not been downloaded.             | Run `ollama pull gemma3:1b`.                                         |
| Unauthorized error when using a `-cloud` model           | You are not signed in to Ollama.               | Run `ollama signin`, then try again.                                 |
| `ModuleNotFoundError: No module named 'ollama'`          | Dependencies are not installed, or the virtual environment is not active. | Run `uv sync`, or activate `.venv` and reinstall the dependencies. |
| Python version error during install                      | The interpreter is older than 3.13.            | Install Python 3.13, or let uv manage it with `uv python install 3.13`. |
| Slow responses                                           | Limited local hardware resources.              | Use a smaller model, or switch to a cloud model.                     |

---

## Contributing

1. Create a feature branch from `main`.
2. Keep each example focused on a single concept, and put it in its own file.
3. Add a short docstring or comments that explain what the example shows.
4. Update the Project Status and Project Structure sections of this README when you add or finish a module.
5. Make sure each script runs successfully before you open a pull request.

---

## Author

**Rizwan**
