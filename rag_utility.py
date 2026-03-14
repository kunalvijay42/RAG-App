import os
from dotenv import load_dotenv

# Old loader (commented): from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

# Loading environment variables from .env file
load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the embedding model
embedding_model = HuggingFaceEmbeddings()

# Loading the llm from Groq
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0)

def process_document_to_chroma_db(file_name):
    # Load the PDF document using PyPDFLoader
    loader = PyPDFLoader(os.path.join(working_dir, file_name))
    documents = loader.load()  # loading the contents of the document

    # Old code (commented) using unstructured pipeline:
    # loader = UnstructuredPDFLoader(os.path.join(working_dir, file_name))
    # documents = loader.load()

    # Split the document into smaller chunks using RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

    texts = text_splitter.split_documents(documents)  # Converting the document to smaller chunks

    #  Store the document chunks in a Chroma vector database
    vectordb = Chroma.from_documents(documents=texts, embedding=embedding_model, persist_directory=os.path.join(working_dir, "doc_vectorstore"))

def answer_query(user_question):
    # Load the Chroma vector database
    vectordb = Chroma(persist_directory=os.path.join(working_dir, "doc_vectorstore"), embedding_function=embedding_model)

    # Create a retriever from the vector database
    retriever = vectordb.as_retriever()

    # Create a RetrievalQA chain using the llm and the retriever
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # Get the answer to the user's question
    # answer = qa_chain.run(user_question)
    answer = qa_chain.invoke(user_question)

    return answer
