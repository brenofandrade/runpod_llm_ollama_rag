import re
# from langchain_community.document_loaders import PDFPlumberLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_answer(text:str) -> str:
    """
    
    """
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def save_uploaded_file(uploaded_file):
    """
    """
    pass

# def load_pdf_documents(file_path):
#     """
#     """
#     document_loader = PDFPlumberLoader(file_path)
#     return document_loader.load()


# def chunk_documents(raw_documents):
#     """
    
#     """

#     text_spliter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30,add_start_index=True)
#     return text_spliter.split_documents(raw_documents)
