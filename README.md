# Generative AI Foundations

A practical, hands-on course on building applications with large language models (LLMs). The repository brings together written lessons, runnable Python examples, interactive notebooks and a backend service. Together they take learners from the core ideas of Generative AI to working applications that use both local and cloud models.

The course is built around three principles:

- **Concept before code.** Each lesson explains an idea with a simple mental model before putting it into practice.
- **Local first.** The examples run on open-weight models through [Ollama](https://ollama.com/), so learners can start without API keys or usage costs.
- **Industry relevance.** Lessons cover the SDKs, API styles and frameworks used in production today, including the OpenAI, Anthropic and Google SDKs, LangChain and LangGraph.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Course Curriculum](#course-curriculum)
- [Lessons Available](#lessons-available)
- [Projects](#projects)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [How to Use This Repository](#how-to-use-this-repository)
- [Project Status](#project-status)
- [Contributing](#contributing)
- [Author](#author)

---

## Repository Structure

```
genai-foundations/
├── docs/                  # Written lessons, organized by module
│   ├── 01-intro-to-genai/
│   ├── 02-how-llms-work/
│   └── 03-prompt-eng/
├── notebooks/             # Interactive Jupyter notebooks that accompany the lessons
│   ├── 01-intro-to-genai/
│   └── 02-how-llms-work/
├── code/                  # Standalone Python examples using the Ollama SDK
├── api/                   # Backend service built on LangChain and Ollama
├── docker-compose.yml     # Multi-service orchestration (planned)
├── .gitignore
└── README.md
```

| Directory      | Purpose                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------- |
| `docs/`        | The main course material. Each lesson is a Markdown file with concepts, diagrams, timelines, setup steps and code examples. |
| `notebooks/`   | Jupyter notebooks for running lesson code step by step and experimenting interactively.     |
| `code/`        | Small, focused Python scripts, each showing one generative AI concept. See [code/README.md](code/README.md). |
| `api/`         | The backend service for the project. See [api/README.md](api/README.md).                   |

---

## Course Curriculum

The course has ten modules. Each module ends with a check-in that tests both concepts and practical skills.

| Module | Topic                                                    | Status      |
| ------ | -------------------------------------------------------- | ----------- |
| 1      | Introduction to Generative AI                            | Available   |
| 2      | How LLMs Work: Tokens, Context Windows, and Limits       | Available   |
| 3      | Prompt Engineering                                       | In progress |
| 4      | Python Setup and Your First API Call                     | Planned     |
| 5      | Working with GenAI SDKs: OpenAI, Claude, Gemini          | Planned     |
| 6      | Structured Output and Text Classification with LLMs      | Planned     |
| 7      | RAG: Answering from Your Own Documents                   | Planned     |
| 8      | Multimodal AI: Image, Audio, and Video                   | Planned     |
| 9      | Responsible AI, Cost, and Quality                        | Planned     |
| 10     | Capstone Project                                         | Planned     |

---

## Lessons Available

### Module 1: Introduction to Generative AI

| Lesson | Title                                                                                        | Topics Covered                                                                          |
| ------ | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 1.1    | [Welcome to Generative AI Foundations](docs/01-intro-to-genai/1.1-introduction-to-generative-ai.md) | What Generative AI is, how it works, its history, multimodal AI, real-world uses, career paths |
| 1.2    | [Generative AI with Ollama](docs/01-intro-to-genai/1.2-generative-ai-with-ollama.md)          | Local and cloud AI, open-weight models, Ollama setup, streaming, a first GenAI script   |
| 1.3    | [Generative AI Python SDKs](docs/01-intro-to-genai/1.3-generative-ai-python-sdks.md)          | Provider SDKs, API styles, managing secrets, streaming, structured output with Pydantic |
| 1.4    | [Check-in](docs/01-intro-to-genai/1.4-check-in.md)                                           | Setup checklist, concept check, code check, mini challenge                              |

### Module 2: How LLMs Work

| Lesson | Title                                                                                                  | Topics Covered                                                                      |
| ------ | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| 2.1    | [Tokens and Tokenization](docs/02-how-llms-work/2.1-tokens-and-tokenization.md)                         | Tokens, Byte Pair Encoding, measuring token usage, LangChain with Ollama            |
| 2.2    | [Context Windows and Memory](docs/02-how-llms-work/2.2-context-windows-and-memory.md)                   | Context windows, stateless models, memory strategies, examples across SDKs          |
| 2.3    | [Generation Settings](docs/02-how-llms-work/2.3-generation-settings.md)                                 | Temperature, top_p, max tokens, reasoning models, recommended settings by task      |
| 2.4    | [Limits of LLMs](docs/02-how-llms-work/2.4-limits-of-llms.md)                                           | Hallucination, knowledge cutoff, cost, latency, a production checklist              |
| 2.5    | [Check-in](docs/02-how-llms-work/2.5-check-in.md)                                                      | Lab checklist, concept check, code check, mini challenge                            |

### Notebooks

| Notebook                                                                                                   | Description                                                   |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [1.1 Introduction to Generative AI](notebooks/01-intro-to-genai/1.1-introduction-to-generative-ai.ipynb)   | A first call to a locally hosted LLM using the Ollama client. |
| [2.1 Tokens and Tokenization](notebooks/02-how-llms-work/2.1-tokens-and-tokenization.ipynb)                 | In progress.                                                  |

---

## Projects

The repository has two independent Python projects. Each manages its own dependencies with [uv](https://docs.astral.sh/uv/).

### code

A collection of focused examples built on the official `ollama` Python library. The current example is a customer support assistant that uses a system prompt and streams its response. Its virtual environment can also be registered as the Jupyter kernel for the notebooks.

Full documentation: [code/README.md](code/README.md)

### api

The backend service for the course. It connects to locally hosted models through LangChain's `langchain-ollama` integration, and it is the foundation for a future HTTP API.

Full documentation: [api/README.md](api/README.md)

---

## Technology Stack

| Category               | Technologies                                                        |
| ---------------------- | ------------------------------------------------------------------- |
| Language               | Python 3.13                                                         |
| Package management     | uv                                                                  |
| Local model runtime    | Ollama                                                              |
| Provider SDKs          | `ollama`, `openai`, `anthropic`, `google-genai`                     |
| Frameworks             | LangChain, LangGraph                                                |
| Data validation        | Pydantic                                                            |
| Tokenization           | `tiktoken`                                                          |
| Configuration          | `python-dotenv`                                                     |
| Interactive learning   | Jupyter (`ipykernel`)                                               |

Each project installs only the packages it needs. Lessons that use the cloud provider SDKs give their own setup steps.

---

## Prerequisites

| Requirement        | Version   | Purpose                                     |
| ------------------ | --------- | ------------------------------------------- |
| Python             | 3.13+     | Runtime for all projects and examples       |
| uv                 | Latest    | Python, package and virtual environment management |
| Ollama             | Latest    | Running models locally                      |
| Git                | Any       | Cloning the repository                      |

Basic Python knowledge is recommended. You need no prior experience with machine learning.

API keys for cloud providers (OpenAI, Anthropic, Google) are **optional**. You only need them for the lessons that use those SDKs.

---

## Quick Start

### 1. Clone the repository

```bash
git clone <repository-url>
cd genai-foundations
```

### 2. Install the core tools

```bash
# uv (macOS and Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ollama (macOS, using Homebrew)
brew install ollama
```

For other platforms, see the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/) and [ollama.com/download](https://ollama.com/download).

### 3. Start Ollama and download a model

```bash
ollama serve
ollama pull gemma3:1b
```

### 4. Run your first example

```bash
cd code
uv sync
uv run main.py
```

A streamed reply from the customer support assistant appears in the terminal. You are now ready to work through the lessons.

---

## How to Use This Repository

1. **Read the lesson.** Start with [Lesson 1.1](docs/01-intro-to-genai/1.1-introduction-to-generative-ai.md) and work through the modules in order.
2. **Run the code.** Type and run each example from the lesson yourself, instead of only reading it.
3. **Experiment in the notebooks.** Change prompts, models and settings to see how the output changes.
4. **Complete the check-in.** Finish each module's check-in before you move on. Try every question before you look at the answers.
5. **Build toward the capstone.** Choose a real problem early and add to your solution as you go through the course.

### Managing Secrets

Lessons that use cloud providers keep API keys in a `.env` file. These files are listed in `.gitignore` and must never be committed. Use the provided `.env.example` files as templates.

---

## Project Status

This repository is under active development. Content is added module by module.

| Area                   | Status                                                     |
| ---------------------- | ---------------------------------------------------------- |
| Modules 1 and 2        | Lessons and check-ins complete                             |
| Module 3 onward        | In progress or planned                                     |
| Notebooks              | Partially complete                                         |
| `code` project         | Initial example implemented; more modules planned          |
| `api` project          | Initial LLM client implemented; HTTP layer planned         |
| Docker support         | Planned                                                    |

---

## Contributing

Contributions that improve accuracy, clarity or coverage are welcome.

1. Create a feature branch from `main`.
2. Follow the existing lesson format: a clear definition, a mental model, tables for comparisons, runnable code, and key takeaways.
3. Keep examples small, focused and runnable on a local Ollama model where possible.
4. Use the existing naming convention for files and folders: `NN-module-name/` for module folders and `N.N-lesson-title.md` for lesson files.
5. Never commit secrets, `.env` files or virtual environments.
6. Check that all code runs and all links work before you open a pull request.

---

## Author

**Rizwan**
