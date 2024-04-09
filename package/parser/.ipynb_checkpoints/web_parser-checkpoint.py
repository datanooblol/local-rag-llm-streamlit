from langchain_community.document_loaders import WebBaseLoader

def get_docs_from_url(url):
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict()
    )
    text = loader.load()
    return text