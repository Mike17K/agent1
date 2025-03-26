# AI Agent with Model Context Protocol (MCP)

## Features
- Retrieval-Augmented Generation (RAG)
- Web Search Integration
- Context-aware Response Generation
- OpenAPI Endpoint for Scalability

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mike17K/agent1.git

## Run
have ollama installed 
ollama serve
ollama run gemma3:4b

pip install -r requirements.txt
uvicorn app.main:app --reload

curl -X POST "http://127.0.0.1:8000/generate/" -H "Content-Type: application/json" -d "{\"query\": \"What is AI?\"}"

## Run Tests
python -m tests.test_web_search
