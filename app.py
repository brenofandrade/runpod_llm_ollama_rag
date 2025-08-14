import os
import shutil
import uuid 

from pathlib import Path
import streamlit as st
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


def reset_chat():
    prompt = None

st.set_page_config(page_title="chat PDF", page_icon="", layout="wide")
st.title("📄 Assitente de documentos da UNIMED Blumenau")



# with st.sidebar:
#     st.button("Reiniciar chat", on_click=reset_chat())


prompt = st.chat_input("Tire suas dúvidas sobre os processos de autorizações...")

if prompt:
    with st.chat_message("user"):
        st.write(f"{prompt}")

    with st.chat_message("ai"):
        st.write("Olá, como posso te ajudar hoje?")


