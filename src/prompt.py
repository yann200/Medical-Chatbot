system_prompt = ("""You are a helpful medical assistant. Use the following context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer."""
                 "\n\n"
                 "{context}")


# check_versions.py
import sys
import os
import langchain
import langchain_community
import langchain_openai
import langchain_pinecone
import sentence_transformers
import huggingface_hub
import flask

print("Python version:", sys.version)
print("OS environment:", os.name)
print("--- Package versions ---")
print("langchain:", langchain.__version__)
print("langchain_community:", langchain_community.__version__)
#print("langchain_openai:", langchain_openai.__version__)
#print("langchain_pinecone:", langchain_pinecone.__version__)
print("sentence-transformers:", sentence_transformers.__version__)
print("huggingface-hub:", huggingface_hub.__version__)
print("flask:", flask.__version__)

