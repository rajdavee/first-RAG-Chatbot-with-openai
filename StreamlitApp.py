import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_openai_embedding
from QAWithPDF.model_api import load_openai_model

def main():
    st.set_page_config("QA with Documents")
    
    doc = st.file_uploader("upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question = st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document = load_data(doc)
            model = load_openai_model()
            query_engine = download_openai_embedding(model, document)
            
            # Create a placeholder for streaming response
            response_placeholder = st.empty()
            
            # Handle streaming response
            response = query_engine.query(user_question)
            full_response = ""
            
            # Stream the response
            for text in response.response_gen:
                full_response += text
                response_placeholder.write(full_response)
                
if __name__ == "__main__":
    main()





