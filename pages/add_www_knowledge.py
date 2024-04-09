import streamlit as st
from package.parser.web_parser import get_docs_from_url
from package.utils import create_documents, list_db_collections
from package.crud.create_and_fetch_vectordb import add_to_vectordb

st.set_page_config(
    page_title="add www knowledge",
)

st.title("Add Knowledge from WWW")


st.session_state['add_www_collection'] = st.selectbox(label="Select or add your collection", options=["add"]+list_db_collections(), index=0)

if st.session_state['add_www_collection']=="add":
    st.session_state['add_www_collection'] = st.text_input(label="Input your collection.")

if len(st.session_state['add_www_collection'])>0:
    url = st.text_input(label="Input your url here", )
    is_add = st.button(label="Add")

    if (len(url)>0) & (is_add==True):
        added_message = f"""
        Successfully added data:\n
        from url - {url}\n
        to collection - {st.session_state['add_www_collection']}
        """
        text = get_docs_from_url(url)
        documents = create_documents(text)
        add_to_vectordb(documents=documents, collection_name=st.session_state['add_www_collection'])
        st.write(added_message)