import streamlit as st
from package.crud.read_vectordb import load_vectordb
from package.utils import get_context, format_context, generate_prompt, list_db_collections
from package.generate_response import ask_llm, llm
from package.query_context import query_single_collection, query_multiple_collections

# from langchain_community.llms import Ollama

# llm = Ollama(base_url = 'http://localhost:11434', model="mistral")

st.set_page_config(
    page_title="query",
)

st.title("Query")

def query_fn():
    st.session_state['query_collections'] = st.multiselect(label="Select collections", options=list_db_collections(), placeholder="Choose one collection or more")

    query = st.text_input(
        "Input your query",
        "",
        key="placeholder",
    )
    is_query = st.button(label="Query")

    if (len(query)>0) & (is_query==True):
        query_collections = st.session_state['query_collections']
        contexts = query_multiple_collections(query, query_collections)
        prompt = generate_prompt(query, contexts)

        with st.expander("Original Query"):
            st.write(query)
        with st.expander("Context from Existing Knowledge"):
            st.write(contexts)
        with st.expander("Augmented Prompt"):
            st.write(prompt)
        with st.expander("Call LLM from langchain"):
            st.write(ask_llm(prompt))
        with st.expander("Call LLM from original lib"):
            st.write(llm.invoke(prompt))

if len(list_db_collections())==0:
    st.write("Please add knowledge to a collection first")
else:
    query_fn()