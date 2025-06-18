from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI()

st.header("Research Tool")

user_input = st.text_input("Enter your research question:")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)

