import os
from langchain_classic.chains import RetrievalQA
import streamlit as st
from rag_utility import process_document_to_chroma_db, answer_query

# Setting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

st.title("RAG Application")

# File Uploader Widget
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    # Define Save Path
    save_path = os.path.join(working_dir, uploaded_file.name)

    #Save the file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    process_document = process_document_to_chroma_db(uploaded_file.name)

    st.info("Document processed Successfully!!")

# Text Widget to get user query
user_question = st.text_area("Ask your question regarding the document:")

if st.button("Answer"):

    answer = answer_query(user_question)

    st.markdown("### 🤖 Agent's Response:")

    st.markdown(answer)