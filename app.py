import streamlit as st
import tempfile
from backend import process_pdf, create_vectorstore, build_qa_chain
from helper import extract_answer

st.set_page_config(page_title="chat PDF", page_icon="", layout="wide")
st.title("📄 Assitente de documentos da UNIMED Blumenau")


def reset_chat():
    """Clear conversation history and reset assistant state."""
    if "assistant" in st.session_state:
        st.session_state["assistant"].clear()
    st.session_state["messages"] = []
    st.session_state["user_input"] = ""

# Sidebar PDF upload
with st.sidebar:
    st.subheader("Upload de Documentos")
    uploaded_file = st.file_uploader("Escolha um arquivo PDF", type=["txt","pdf"], accept_multiple_files=True)

    st.button("Reiniciar Chat", on_click=reset_chat, use_container_width=True)

# Load and embed docs
if uploaded_file:
    if "qa_chain" not in st.session_state:
        with st.spinner("Processando documentos..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            docs = process_pdf(tmp_file_path)
            vectorstore = create_vectorstore(docs)
            st.session_state.qa_chain = build_qa_chain(vectorstore)
            st.session_state.conversation = []

    qa_chain = st.session_state.qa_chain
    st.success("Documentos processados e indexados! Faça sua pergunta.")

    # Chat Interface
    st.markdown("### 💬 Pergunte algo sobre o documento")

    for q, a in st.session_state.conversation:
        st.write("**Pergunta:**", q)
        st.write("**Resposta:**", a)
        st.markdown("---")

    user_input = st.text_input("Sua pergunta:", key="user_question")

    if user_input:
        with st.spinner("Pensando..."):
            response = qa_chain.invoke(user_input)
            final_response = extract_answer(response['result'])

        st.session_state.conversation.append((user_input, final_response))
        
