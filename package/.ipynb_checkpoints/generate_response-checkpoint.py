from langchain_community.llms import Ollama

import ollama

def ask_llm(prompt):
    response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

llm = Ollama(base_url = 'http://localhost:11434', model="mistral")

# llm = Ollama(base_url = 'http://ollama-container:11434', model="mistral")
