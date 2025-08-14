import os
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader, TextLoader, UnstructuredFileLoader
)
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate
from langchain.retrievers import EnsembleRetriever

# Configuração
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
GENERATIVE_MODEL = os.getenv("GEN_MODEL", "llama3.2")
EMBEDDING_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "2000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "300"))

print(
    '\nLLM:', GENERATIVE_MODEL,
    '\nEmbedding:', EMBEDDING_MODEL,
    '\nChunk:', CHUNK_SIZE, "size", CHUNK_OVERLAP, "overlap\n",
    
    "="*50
)


def get_llm():
    return ChatOllama(
        model=GENERATIVE_MODEL,
        base_url=OLLAMA_HOST,
        temperature=0,
        num_ctx=8192,
    )

def get_embeddings():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_HOST
    )

