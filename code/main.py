from ollama import chat


MODEL = "gemma3:1b"  # change to "gemma4:31b-cloud" to use the cloud

SYSTEM_PROMPT = (
    "You are a professional customer support assistant for an online store. "
    "Reply politely, give clear next steps, and keep answers under 80 words."
)


def ask_support(question: str) -> None:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    stream = chat(model=MODEL, messages=messages, stream=True)

    for chunk in stream:
        print(chunk.message.content, end="", flush=True)
    print()


if __name__ == "__main__":
    ask_support("My order arrived damaged. What should I do?")
