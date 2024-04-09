import streamlit as st
from package.crud.read_vectordb import load_vectordb
from package.utils import get_context, format_context, generate_prompt, list_db_collections
from package.generate_response import ask_llm

from langchain_community.llms import Ollama

st.set_page_config(
    page_title="Main Page",
)

st.title("Main Page")