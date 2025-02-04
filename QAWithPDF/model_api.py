import os
from langchain_openai import OpenAI  # Updated import
from dotenv import load_dotenv
import sys

from IPython.display import Markdown, display
from exception import customexception
from logger import logging

load_dotenv()

def load_openai_model():
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        model = OpenAI(
            temperature=0.7, 
            openai_api_key=api_key,
            model="gpt-3.5-turbo-instruct"  # Specify model explicitly
        )
        return model
    except Exception as e:
        raise customexception(e, sys)
