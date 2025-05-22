
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st





template="""
Answer the question below:

here is the conversation history: {context}

Question:{question}
Ans: 

"""

model=OllamaLLM(model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF")
prompt=ChatPromptTemplate.from_template(template)

chain=prompt | model


# Initialize session state
if "context" not in st.session_state:
    st.session_state.context = ""

st.title("🧠 AI Chatbot")

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    # Invoke model
    result = chain.invoke({"context": st.session_state.context, "question": user_input})

    # Show response
    st.write("🤖:", result)

    # Update context
    st.session_state.context += f"\nUser: {user_input}\nAI: {result}\n"