# Notes

Your working directory should be:  
> local-rag-llm-streamlit/

For jupyter lab implementation:
- run command: jupyter lab  

For Streamlit implementation:
- run command: streamlit run ui.py

For Docker implementation:
- open your CLI
- go to the folder containing docker-compose.yaml
- run command: docker-compose up
- open another CLI (only for the first time)
- run command: docker exec -it "your-container-name" ollama run "model-name"  

The docker solution is in progress.  
Please be patient  