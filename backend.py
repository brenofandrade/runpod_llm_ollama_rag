# backend.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

import os
from typing import List

# Initialize embedding model
# embeddings = HuggingFaceEmbeddings(model_name="nomic-ai/nomic-embed-text-v1")
embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")
# Load Ollama model (ensure Ollama is running and llama3 is pulled)
llm = ChatOllama(model="deepseek-r1:latest", temperature=0.2)



# Load and split document
def process_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    return split_docs

# Create or load vector store
def create_vectorstore(documents):
    db = FAISS.from_documents(documents, embeddings)
    return db

# Build QA chain
def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
