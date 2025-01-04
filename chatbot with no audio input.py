import json
import os 
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template_general = """
you are a Personal AI made by Aakash Sharma.
About Aakash Sharma: Aakash Sharma was born on july 22nd 2005 and is currently pursing BCA in data Science and is working on ai chatbot which will soon have voice recognition.

Answer the question below:

Here is the conversation history: {context}

Question: {question}

Answer:
"""

try:
    model = OllamaLLM(model ="mistral")
except:
    os.system('ollama run mistral')
prompt = ChatPromptTemplate.from_template(template=template_general)
chain = prompt | model

def create_new_conversation_history():
    pass

def load_conversation_history(filename="conversation_history.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        with open(filename , "w") as file:
            json.dump({}, file)
        return{}
def save_conversation_history(history , filename = "conversation_history.json"):
    with open(filename, "w") as file:
        json.dump(history , file, indent= 4)

def handle_conversation():
    conversation_history = load_conversation_history()
    context = ""
    if conversation_history:
        for user_input, result in conversation_history.items():
            context += f"{user_input}\nAI: {result}\n"
    print("hello sire ")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        else:
                if user_input in conversation_history:
                    result = conversation_history[user_input]
                    print("Droud1:",result)
                else:
                    result = chain.invoke({"context": context, "question": user_input})
                    print("Droud1:",result)
                    conversation_history[user_input] = result
        context = f"\nUser: { user_input}\nAI: {result}"
        
        save_conversation_history(conversation_history)
        print("\n")
        

handle_conversation()
