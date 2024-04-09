import chromadb

def delete_collection(persist_directory="./vectordb", collection_name=""):
    client = chromadb.PersistentClient(path=persist_directory)
    client.delete_collection(name=collection_name)