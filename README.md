# 📄 PDF RAG Application
 
A **Retrieval-Augmented Generation (RAG)** application that lets you upload any PDF document and ask natural language questions about its content — powered by Groq LLM, ChromaDB, and Hugging Face embeddings.
 
---
 
## 🚀 Demo
 
> Upload a PDF → Ask any question → Get context-aware answers instantly
 
---
 
## 🏗️ Architecture
 
```
PDF Document
     │
     ▼
┌─────────────────┐
│  PDF Ingestion  │  Extract raw text from uploaded PDF
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Chunking   │  Split document into overlapping chunks
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│ Hugging Face Embedding Model │  Convert chunks → dense vectors
└────────────┬────────────────┘
             │
             ▼
┌─────────────────┐
│    ChromaDB     │  Store and index vector embeddings
└────────┬────────┘
         │
    User Query
         │
         ▼
┌─────────────────────────────┐
│  Semantic Similarity Search  │  Retrieve top-k relevant chunks
└────────────┬────────────────┘
             │
             ▼
┌─────────────────┐
│    Groq LLM     │  Generate context-aware response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Streamlit UI   │  Display answer to user
└─────────────────┘
```
 
---
 
## 🛠️ Tech Stack
 
| Component | Technology |
|---|---|
| **LLM** | Groq (llama-3.1-8b-instant) |
| **Embeddings** | Hugging Face Sentence Transformers |
| **Vector Database** | ChromaDB |
| **Frontend UI** | Streamlit |
| **Language** | Python 3.11 |
 
---
 
## ✨ Features
 
- 📁 Upload any PDF document via drag-and-drop UI
- 🔍 Semantic search across document content using vector embeddings
- ⚡ Fast LLM inference powered by Groq API
- 💬 Interactive Q&A interface built with Streamlit
- 🧠 Context-aware responses grounded in your document — no hallucinations from unrelated data
- 🗄️ Persistent vector storage with ChromaDB
 
---
 
## 📁 Project Structure
 
```
RAG-App/
├── app.py               # Streamlit UI and application entry point
├── rag_utility.py       # Core RAG logic — chunking, embedding, retrieval
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```
 
---
 
## ⚙️ Setup & Installation
 
### 1. Clone the repository
```bash
git clone https://github.com/kunalvijay42/RAG-App.git
cd RAG-App
```
 
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```
 
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
 
### 4. Set up environment variables
 
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
 
Get your free Groq API key at [console.groq.com](https://console.groq.com)
 
### 5. Run the application
```bash
streamlit run app.py
```
 
Open your browser at `http://localhost:8501`
 
---
