from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI(    model_name="gpt-3.5-turbo",  # Specify the model name
    temperature=1.5,  # Set the temperature for randomness in responses
    max_tokens=100)

st.header("Research Tool")

user_input = st.text_input("Enter your research question:")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)

