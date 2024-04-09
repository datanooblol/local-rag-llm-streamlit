from package.crud.read_vectordb import load_vectordb
from package.utils import get_context, format_context

def query_single_collection(query:str, persist_directory:str="./vectordb", collection=None):
    vectordb = load_vectordb(persist_directory=persist_directory, collection_name=collection)
    context = get_context(query, vectordb)
    context = format_context(context)
    return context

def query_multiple_collections(query:str, collections:list):
    contexts = []
    for collection in collections:
        context = query_single_collection(query=query, persist_directory="./vectordb", collection=collection)
        contexts.append(context)
    contexts = "\n\n".join(contexts)
    return contexts