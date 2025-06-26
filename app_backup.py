# from langchain_community.document_loaders import PDFPlumberLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.vectorstores import InMemoryVectorStore
# from langchain_ollama import OllamaEmbeddings
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama.llms import OllamaLLM



from helper import *

PDF_STORAGE_PATH = 'data/'
# EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:latest")
# DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
# LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:latest")



# 



# DOCUMENT_VECTOR_DB.add_documents(document_chunks)
    



### UI Config


# import streamlit as st


# st.set_page_config(
#     page_title="Unimed",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("Chat Unimed 📘")
# st.write("Assitente de inteligência para documentos!")
# st.markdown("---")


# with st.sidebar:

#     uploaded_pdf = st.file_uploader(
#         label="Selecione um documento (PDF)",
#         type="pdf",
#         accept_multiple_files=False
#     )


import streamlit as st

st.set_page_config(
    page_title="Unimed Chat RAG",
    page_icon="🤖",
    layout="wide"
)

# -------------------- TÍTULO E DESCRIÇÃO --------------------
st.title("📘 Chat Unimed - Assistente de Documentos")
st.caption("Um assistente inteligente para responder perguntas com base em documentos da Unimed.")

st.markdown("---")

# -------------------- LAYOUT PRINCIPAL --------------------
col1 = st.columns([1], gap="large")

# Upload de PDF e parâmetros na coluna lateral
with st.sidebar:
    st.header("📂 Documento")
    uploaded_pdf = st.file_uploader(
        label="Envie um documento PDF",
        type="pdf",
        accept_multiple_files=False
    )

    st.markdown("---")
    st.header("⚙️ Parâmetros do Modelo")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.2, 0.1)
    max_tokens = st.slider("Máximo de Tokens", 100, 1000, 500, 50)

    st.markdown("---")
    if uploaded_pdf:
        st.success("Documento carregado com sucesso!")
    else:
        st.info("Aguardando envio de documento...")

# Campo de chat e resposta

st.subheader("💬 Converse com o assistente")

user_question = st.text_input("Digite sua pergunta:", placeholder="Ex: Quais são as coberturas do plano?")

if st.button("Perguntar"):
    if uploaded_pdf and user_question:
        st.info("🔍 Processando sua pergunta com RAG...")
        # Aqui entraria a chamada para o backend RAG com embeddings
        # resposta = seu_modelo_rag(resposta)
        st.success("✅ Resposta gerada com sucesso!")
        st.write("**Resposta:** Aqui está a resposta simulada baseada no documento.")
    else:
        st.warning("Por favor, envie um documento e digite uma pergunta.")






# Rodapé
st.markdown("---")
st.caption("Desenvolvido com ❤️ pela equipe de dados da Unimed")
