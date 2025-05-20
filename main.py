
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate





template="""
Answer the question below:

here is the conversation history: {context}

Question:{questions}
Ans: 

"""

model=OllamaLLM(model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF")
prompt=ChatPromptTemplate.from_template(template)

chain=prompt | model


def handle_conversatiton():
    context=""
    print("Welcome to AI Chat bot")
    while True:
        user_input=input("you: ")
        if user_input.lower()=="exit":
            break
        result=chain.invoke({"context":"", "questions":user_input})
        print("bot: ", result)
        context+=f"\nUser: {user_input}\nAI:{result}"


if __name__=="__main__":
    handle_conversatiton()