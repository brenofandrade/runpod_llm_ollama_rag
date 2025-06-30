from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.utils import filter_complex_metadata
from typing import List, Tuple

class ChatPDF:
    vector_store = None
    retriever = None
    chain = None
    chat_history: List[Tuple[str, str]]

    def __init__(self):
        self.model = ChatOllama(model="mistral")
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
        self.chat_history = []
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] Você é um assistente de RAG. Utilize o histórico de conversa e o contexto do documento para responder de forma objetiva. Caso não saiba a resposta, informe que não sabe. [/INST] </s>
            Histórico:
            {history}
            [INST] Pergunta: {question}
            Contexto: {context}
            Resposta: [/INST]
            """
        )

    def ingest(self, pdf_file_path: str):
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        chunks = self.text_splitter.split_documents(docs)
        chunks = filter_complex_metadata(chunks)

        vector_store = Chroma.from_documents(documents=chunks, embedding=FastEmbedEmbeddings())
        self.retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )

        self.chain = ({
            "context": self.retriever,
            "question": RunnablePassthrough(),
            "history": lambda x: x.get("history", ""),
        }
                      | self.prompt
                      | self.model
                      | StrOutputParser())

    def ask(self, query: str):
        if not self.chain:
            return "Please, add a PDF document first."

        history_text = ""
        for q, a in self.chat_history:
            history_text += f"Usuário: {q}\nAssistente: {a}\n"

        answer = self.chain.invoke({"question": query, "history": history_text})
        self.chat_history.append((query, answer))
        return answer

    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None
        self.chat_history = []
