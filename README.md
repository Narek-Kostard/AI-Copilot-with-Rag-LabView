# LabVIEW RAG Chatbot with Ollama + Qdrant

A lightweight **Retrieval-Augmented Generation (RAG)** chatbot that answers questions about **LabVIEW** using a local vector database (Qdrant) and local LLMs via **Ollama**.

When the user asks something related to LabVIEW, the bot automatically retrieves the most relevant chunks from a LabVIEW knowledge base and injects them as context to the LLM (Mistral by default). For non-LabVIEW questions it works as a regular chatbot.

Everything runs **100% locally** – no API keys, no cloud costs.

## Features

- Local embedding model (`nomic-embed-text`)
- Local LLM (`mistral` or any other Ollama model)
- Persistent vector store with **Qdrant** (Docker or native)
- Simple keyword detection to activate RAG only for LabVIEW-related queries
- Ready-to-run Python scripts
- Easy re-indexing of new LabVIEW documentation

## Tech Stack

- **Ollama** – running `nomic-embed-text` and `mistral` (or any other model)
- **Qdrant** – vector database (runs on `http://localhost:6333`)
- **Python 3.10+**
- `ollama` python package + `qdrant-client`

## Project Structure
├── main-logic.py          → Main chatbot logic (RAG + conversation history)
├── create_collection.py → Creates/recreates the Qdrant collection
├── chunking.py          → Splits raw text (output.txt) into chunks → labview_chunks.json
├── chunk_to_embedding.py→ Generates embeddings and uploads them to Qdrant
├── #Documentation           → Your raw LabVIEW documentation (you provide this)
├── chunk-name.json  → Intermediate JSON with chunks (auto-generated)

## Prerequisites

1. **Ollama** installed and running  
   ```bash
   # Install Ollama: https://ollama.com/download
   ollama pull nomic-embed-text
   ollama pull mistral   # or any other model you prefer


##Qdrant running locally (the easiest way is Docker):
- docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant

##Example input (JSON)
{
  "History": [
    {"role": "user", "content": "What is LabVIEW?"},
    {"role": "assistant", "content": "LabVIEW is a graphical programming platform..."}
  ],
  "content": "How do I create a simple VI that adds two numbers?"


#Enjoy your private, offline LabVIEW expert!
