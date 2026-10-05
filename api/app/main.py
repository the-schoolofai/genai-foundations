from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.7,
)

response = llm.invoke("Hi")
print(response.content)
