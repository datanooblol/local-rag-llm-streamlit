def create_prompt(query, vectordb):
    context = vectordb.as_retriever().invoke(query)
    context = format_context(context)
    # prompt = f"Question: {query}\n\nContext: {context}"
    prompt = f"Query: {query}\n\nContext: {context}"
    return prompt