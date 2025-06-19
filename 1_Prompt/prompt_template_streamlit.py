from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model
model = ChatOpenAI()

# Streamlit app header
st.header("Greeting Tool")
user_input = st.text_input("Enter your name:")

# If the button is clicked, invoke the model with the prompt
if st.button("Greet"):
    # Create a prompt template with a placeholder for the name
    template = PromptTemplate(
        template="Greet this person in 5 different languages including hindi. The name of the person is {name}",
        input_variables=["name"]
    )
    
    # Fill the values of the placeholders
    prompt = template.format(name=user_input)
    
    # Invoke the model with the filled prompt
    result = model.invoke(prompt)
    
    # Display the result in the Streamlit app
    st.write(result.content)

