import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_context(query, vectordb):
    context = vectordb.as_retriever().invoke(query)
    return context

def format_context(context):
    text = "\n\n"
    context = text.join(cntx.page_content for cntx in context)
    return context

def generate_prompt(query, context):
    prompt = f"Query: {query}\n\nContext: {context}"
    return prompt

def list_db_collections(path="./vectordb"):
    client = chromadb.PersistentClient(path=path)
    collections = client.list_collections()
    return [collection.name for collection in collections]

def create_documents(text):    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(text)
    return documents