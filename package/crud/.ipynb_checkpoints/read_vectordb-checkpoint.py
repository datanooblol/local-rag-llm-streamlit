from package import embeddings
from langchain_community.vectorstores import Chroma

def load_vectordb(embeddings=embeddings, persist_directory="./vectordb", collection_name='roo'):
    vectordb = Chroma(
        embedding_function=embeddings,
        persist_directory=persist_directory, 
        collection_name=collection_name, 
    )
    return vectordb