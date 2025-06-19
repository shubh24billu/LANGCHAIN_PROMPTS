from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI( 
    model_name="gpt-3.5-turbo",  # Specify the model name
    temperature=1.5,  # Set the temperature for randomness in responses
    max_tokens=50  # Set the maximum number of tokens in the response
)

# detailed way
template2 = PromptTemplate(
    template='Tell me about this device {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':"mobile phone"})

result = model.invoke(prompt)

print(result.content)
