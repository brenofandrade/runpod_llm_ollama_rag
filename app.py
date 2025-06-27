import streamlit as st
import tempfile
from backend import process_pdf, create_vectorstore, build_qa_chain
from helper import extract_answer

st.set_page_config(page_title="chat PDF", page_icon="", layout="wide")
st.title("📄 Assitente de documentos da UNIMED Blumenau")

# Sidebar PDF upload
with st.sidebar:
    st.subheader("Upload de Documentos")
    uploaded_file = st.file_uploader("Escolha um arquivo PDF", type=["txt","pdf"])

# Load and embed docs
if uploaded_file:
    with st.spinner("Processando documentos..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        docs = process_pdf(tmp_file_path)
        vectorstore = create_vectorstore(docs)
        qa_chain = build_qa_chain(vectorstore)

        st.success("Documentos processados e indexados! Faça sua pergunta.")

        # Chat Interface
        st.markdown("### 💬 Pergunte algo sobre o documento")
        user_input = st.text_input("Sua pergunta:", key="user_question")

        if user_input:
            with st.spinner("Pensando..."):
                response = qa_chain.invoke(user_input)
                final_response = extract_answer(response['result'])

                print("Response:",response)
                print("--- "*5)
                print("Resposta Final:",final_response)

                st.write("🧠 Resposta:", response)
                st.markdown("---")
                st.write("Resposta:", final_response)
