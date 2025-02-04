from llama_index.core import VectorStoreIndex
from llama_index.core.settings import Settings
from llama_index.llms.langchain import LangChainLLM
from llama_index.embeddings.openai import OpenAIEmbedding
import sys
from exception import customexception
from logger import logging

def download_openai_embedding(model, documents):
    try:
        logging.info("Initializing OpenAI embedding model")
        embed_model = OpenAIEmbedding()
        llm = LangChainLLM(llm=model)
        
        logging.info("Configuring Settings")
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        Settings.embed_model = embed_model
        Settings.llm = llm
        
        logging.info("Creating VectorStoreIndex")
        index = VectorStoreIndex.from_documents(
            documents,
            show_progress=True  # Add progress bar
        )
        
        logging.info("Creating Query Engine")
        return index.as_query_engine(
            streaming=True,
            response_mode="compact"  # Changed from tree_summarize
        )
    except Exception as e:
        raise customexception(e, sys)
