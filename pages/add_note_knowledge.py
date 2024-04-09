import streamlit as st
from package.parser.web_parser import get_docs_from_url
from package.utils import create_documents, list_db_collections
from package.crud.create_and_fetch_vectordb import add_to_vectordb
from langchain_core.documents.base import Document

st.set_page_config(
    page_title="add note knowledge",
)

st.title("Add Knowledge from note")


st.session_state['add_content_collection'] = st.selectbox(label="Select or add your collection", options=["add"]+list_db_collections(), index=0)

if st.session_state['add_content_collection']=="add":
    st.session_state['add_content_collection'] = st.text_input(label="Input your collection.")

if len(st.session_state['add_content_collection'])>0:
    page_content = st.text_input(label="Input your content here", )
    source = st.text_input(label="Source", )
    page = st.text_input(label="Page", )
    line = st.text_input(label="Line", )
    
    is_add = st.button(label="Add")

    if (len(page_content)>0) & (is_add==True):
        documents = Document(
            page_content=page_content,
            metadata={
                'source':source,
                'page':page,
                'line':line,
            }
        )

        added_message = f"""
        Successfully added content:\n
        -----
        
        {page_content}

        -----
        to collection - {st.session_state['add_content_collection']}
        """

        add_to_vectordb(documents=[documents], collection_name=st.session_state['add_content_collection'])
        st.write(added_message)
