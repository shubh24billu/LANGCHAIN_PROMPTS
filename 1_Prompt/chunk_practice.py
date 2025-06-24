import re


paragraph = """
LangChain is a powerful framework for building applications with language models. 
It supports prompt chaining, retrieval-based generation, and tool integration. 
OpenAI models like GPT-4 are commonly used in LangChain pipelines. 
Before passing documents to a model, they must be split into manageable chunks. 
This often involves sentence splitting, chunk grouping, and embedding generation. 
Vector databases store these chunks for fast retrieval using semantic similarity.
"""

print(re.split(r'(?<=[.!?])+',paragraph.strip()))
