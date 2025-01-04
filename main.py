from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import templates

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer
"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template=template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Deroid 1: Hi, I am Deroid 1")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
    result = chain.invoke({"context":context,"question":user_input})
    print("Deroid 1: ", result)
    context += f"\n User: {user_input}\nDeroid 1: {result}"

if __name__ == "__main__":
    handle_conversation()

