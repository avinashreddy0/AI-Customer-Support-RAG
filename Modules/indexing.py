import streamlit as st
import glob 
from config import DATA_PATH,CHUNK_SIZE,CHUNK_OVERLAP,EMBEDDING_MODEL,COLLECTION_NAME,CHROMA_PATH
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

@st.cache_resource
def indexing_file():
    documents = []
    PDFs = glob.glob(f"{DATA_PATH}/**/*.pdf",recursive=True)
    for pdf in PDFs:
        files = PyPDFLoader(pdf)
        doc = files.load()
        documents.extend(doc)

    splitting = RecursiveCharacterTextSplitter(chunk_size = CHUNK_SIZE,chunk_overlap = CHUNK_OVERLAP)
    chunks = splitting.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name = EMBEDDING_MODEL)

    test_embedding = embedding.embed_query("test customer support")
    print(len(test_embedding))

    if not test_embedding:
        raise ValueError("Embedding model returned an empty embedding.")

    vector_database = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME
    )

    return vector_database


