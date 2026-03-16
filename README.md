# 🤖 CrewAI RAG Chatbot

> An intelligent document Q&A chatbot powered by the **CrewAI** framework — upload your PDFs or DOCX files and get precise, context-aware answers. Runs entirely on **free, open-source models** via Hugging Face.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Framework-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Qwen%20%7C%20SentenceTransformers-yellow?logo=huggingface)
![Langfuse](https://img.shields.io/badge/Langfuse-Tracing-purple)


---

##  Overview

The **CrewAI RAG Chatbot** is a Retrieval-Augmented Generation (RAG) system that lets users upload their own documents and ask natural language questions about them. It uses a **single CrewAI agent** equipped with a **RAG SearchTool** to retrieve relevant chunks from the document and generate accurate answers — no paid API required.

Key highlights:
-  Upload **PDF** or **DOCX** files and query their content instantly
-  Fully free — powered by **Qwen (Hugging Face)** as the LLM and **Sentence Transformers** for embeddings
-  Maintains **session-based conversation history** and short-term memory for contextual accuracy
-  Integrated with **Langfuse** for full agent performance tracing and debugging

---

##  Features

| Feature | Description |
|---|---|
|  Document Upload | Supports PDF and DOCX file ingestion |
|  Single RAG Agent | One CrewAI agent with a SearchTool that retrieves and answers from your document |
|  Conversation Memory | Full history + short-term context window per user session |
|  Session Management | Database-backed user sessions for persistent interactions |
|  Performance Tracing | Langfuse integration for agent behavior analysis and latency optimization |
|  Web UI | Clean Streamlit interface with multi-page navigation |

---

##  Project Structure
```
CrewAI-RAG-Chatbot/
├── app.py                  # Main Streamlit entry point
├── pages/                  # Multi-page Streamlit app pages
├── src/
│   ├── chatbot.py          # Main CrewAI Implementation
│   └── database.py         # Session management and conversation persistence
├── utils/                  # Helper utilities 
├── images/                 # UI assets
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not committed)
```

---

##  Data Flow
```
User Input
    ↓
streamlit_app.py  →  renders chat input and manages UI state
    ↓
chatbot.py (run_agent_query)  →  passes query to the CrewAI agent
    ↓
Agent processes query using RAG SearchTool  →  retrieves relevant document chunks and generates answer
    ↓
chatbot.py (extract_referenced_pages)  →  identifies source pages from retrieved chunks
    ↓
streamlit_app.py  →  displays answer and referenced pages to the user
    ↓
database.py (persist_messages_to_db)  →  saves conversation turn to the session DB
```

---

##  Getting Started

### Prerequisites

- Python 3.10+
- A [Hugging Face account](https://huggingface.co/) and access token (free)
- Langfuse account (optional, for tracing)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/MariAnwar/CrewAI-RAG-Chatbot-.git
   cd CrewAI-RAG-Chatbot-
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Configure environment variables**

   Create a `.env` file in the root directory:
```env
   # Hugging Face — required for LLM (Qwen) and embeddings (Sentence Transformers)
   HUGGINGFACE_API_TOKEN=your_huggingface_token

   # Langfuse tracing (optional)
   LANGFUSE_SECRET_KEY=your_langfuse_secret_key
   LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
   LANGFUSE_HOST=https://cloud.langfuse.com
```

5. **Run the application**
```bash
   streamlit run app.py
```

---

##  Usage

1. Open the app in your browser 
2. Upload a **PDF** or **DOCX** file using the upload panel
3. Type your question in the chat input
4. The agent will search your document and return a context-aware answer
5. Continue the conversation — the chatbot remembers the full session history

---

##  How It Works

The system uses a **single CrewAI agent** equipped with a **RAG SearchTool**. When a question is submitted, the agent uses the tool to search the vector store (ChromaDB) built from the uploaded document, retrieves the most relevant chunks, and generates an answer grounded in that content. No separate retriever and responder agents — one agent handles the full pipeline.

- **LLM:** Qwen (via Hugging Face Inference API)
- **Embeddings:** Sentence Transformers (via Hugging Face)
- **Vector Store:** Built at upload time from the document chunks
- **Memory:** Short-term context is maintained per session; full history is persisted in the database

---

##  Observability with Langfuse

This project uses **Langfuse** to trace every agent interaction, enabling:

-  Visibility into retrieval quality and agent reasoning steps
-  Debugging of complex multi-turn interactions
-  Latency profiling and retrieval speed optimization
-  Usage analytics per session

---

##  Tech Stack

- **[CrewAI](https://docs.crewai.com/)** — Single-agent orchestration with RAG SearchTool
- **[Streamlit](https://streamlit.io/)** — Web UI
- **[Qwen (Hugging Face)](https://huggingface.co/Qwen)** — LLM (free, no OpenAI key needed)
- **[Sentence Transformers](https://www.sbert.net/)** — Embedding model (free, via Hugging Face)
- **[Langfuse](https://langfuse.com/)** — LLM observability and tracing
- **SQLite / SQL DB** — Session and conversation history storage

---

---

##  Contributers

- Maria Anwar
- Salma Ahmed
- Etedal Abughanem

---

