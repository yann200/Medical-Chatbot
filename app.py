from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")



index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=download_embeddings()
)


system_prompt = ("""You are a helpful medical assistant. Use the following context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answers."""
                 "\n\n"
                 "{context}")

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

chatModel = ChatOpenAI(model_name="gpt-3.5-turbo")

question_answer_chain = create_stuff_documents_chain(
    chatModel,
    prompt=prompt)

rag_chain = create_retrieval_chain(retriever, question_answer_chain)



@app.route('/')
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])
    





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
