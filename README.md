
# AI Support Ticket Triage Agent

This project implements an **AI-powered Support Ticket Triage System** using:

- **FastAPI** (backend API)
- **Gemini LLM (Google Generative AI)** for ticket understanding
- **Keyword-based KB search** tool
- **Docker support**
- **Pytest unit tests**
- **Streamlit UI** for demo interface

This project fulfills the complete requirements of the assignment.

#  Project Structure
```bash

triage_agent/
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── llm_client.py
│   ├── kb_search.py
│   ├── config.py
│   └── __init__.py
│
├── kb/
│   └── knowledge_base.json
│
├── tests/
│   ├── test_api.py
│   ├── test_kb_search.py
│   └── __init__.py
│
├── ui.py               ← Streamlit User Interface
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```
---
# Installation

## 1. Create virtual environment
```bash
python -m venv venv,
source venv/bin/activate, 
Windows: venv\Scripts\activate 
```
## 2. Install dependencies
```bash
pip install -r requirements.txt
```
## 3. Configure .env file
```env
GEMINI_API_KEY=your_gemini_key, 
GEMINI_MODEL=gemini-2.5-flash
```
---

# Running FastAPI Backend
```bash
uvicorn app.main:app --reload --port 8000
```
### Test endpoints:

- http://localhost:8000/health
- http://localhost:8000/docs

---

# Run Streamlit UI
```bash

streamlit run ui.py  
Open UI at: http://localhost:8501
```
---

# 🧪 Run Tests
```bash
pytest
```

---

# Docker Run
```bash
docker build -t triage-agent .
docker run -p 8000:8000 --env-file .env triage-agent
```
---

# How the Triage Agent Works

1. User submits support ticket  
2. Gemini LLM extracts:
   - summary  
   - category  
   - severity  
   - suggested next steps  
   - clarifying questions  
3. KB search finds similar issues  
4. Agent classifies:
   - known_issue  
   - new_issue  
5. Returns structured JSON response  


