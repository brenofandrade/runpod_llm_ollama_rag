# app.py

import streamlit as st
from backend import process_pdf, create_vectorstore, build_qa_chain
import tempfile
import os

from helper import extract_answer

st.set_page_config(page_title="RAG with Ollama", layout="wide")
st.title("📄 Chat with PDF using 🦙 Ollama + LangChain + FAISS")

# Sidebar PDF upload
with st.sidebar:
    st.subheader("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Load and embed docs
if uploaded_file:
    with st.spinner("Processing document..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        docs = process_pdf(tmp_file_path)
        vectorstore = create_vectorstore(docs)
        qa_chain = build_qa_chain(vectorstore)

        st.success("Document processed and indexed! Ask your questions below.")

        # Chat Interface
        st.markdown("### 💬 Pergunte algo sobre o documento")
        user_input = st.text_input("Your question:", key="user_question")

        if user_input:
            with st.spinner("Thinking..."):
                response = qa_chain.invoke(user_input)
                final_response = extract_answer(response['result'])

                print("Response:",response)
                print("--- "*5)
                print("Resposta Final:",final_response)

                st.write("🧠 Resposta:", response)
                st.markdown("---")
                st.write("Resposta:", final_response)
