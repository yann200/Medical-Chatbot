FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

# Installer les packages avec versions fixes
RUN pip install --upgrade pip
RUN pip install langchain==0.3.26 \
                langchain-community==0.3.26 \
                huggingface-hub==0.36.0 \
                flask==3.1.1 \
                pypdf==5.6.1\
                python-dotenv==1.1.0\
                langchain-pinecone==0.2.8\
                langchain-openai==0.3.24\
                sentence-transformers==5.2.0 \
CMD ["python3", "app.py"]