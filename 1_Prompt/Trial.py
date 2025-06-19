import re

# Sample input paragraph (could be a document chunk in RAG)
paragraph = """
LangChain is a powerful framework for building applications with language models. 
It supports prompt chaining, retrieval-based generation, and tool integration. 
OpenAI models like GPT-4 are commonly used in LangChain pipelines. 
Before passing documents to a model, they must be split into manageable chunks. 
This often involves sentence splitting, chunk grouping, and embedding generation. 
Vector databases store these chunks for fast retrieval using semantic similarity.
"""

# Step 1: Split paragraph into sentences
sentences = re.split(r'(?<=[.!?]) +', paragraph.strip())

# Step 2: Group into chunks of 3 sentences
chunk_size = 1
for i in range(0, len(sentences),chunk_size):
    chunks = ' '.join(sentences[i:i+chunk_size])
#chunks = [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
print(chunks)
print("List of Chunks:\n")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")
