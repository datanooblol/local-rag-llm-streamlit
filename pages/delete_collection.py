import streamlit as st
from package.utils import list_db_collections
import chromadb
from package.crud.delete_vectordb_collection import delete_collection

st.title("Delete")

def delete_collection_fn():
    st.session_state['deleted_collection'] = st.selectbox(label="Select the collection you want to delete", options=list_db_collections())
    is_delete = st.button(label="Delete")

    if (is_delete==True):
        delete_collection(collection_name=st.session_state['deleted_collection'])
        text = f"""
        Successfully deleted collection: {st.session_state['deleted_collection']}
    """
        st.write(text)    

if len(list_db_collections())==0:
    st.write("You don't have any collections to delete.")
else:
    delete_collection_fn()