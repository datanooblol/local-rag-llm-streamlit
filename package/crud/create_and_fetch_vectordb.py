from package import embeddings
from langchain_community.vectorstores import Chroma

def add_to_vectordb(documents=None, embeddings=embeddings, persist_directory="./vectordb", collection_name=None):
    db = Chroma.from_documents(
        documents=documents, 
        embedding=embeddings, 
        persist_directory=persist_directory, 
        collection_name=collection_name
    )

