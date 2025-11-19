
# 🚀 AI Support Ticket Triage Agent

This project implements an **AI-powered Support Ticket Triage System** using:

- **FastAPI** (backend API)
- **Gemini LLM (Google Generative AI)** for ticket understanding
- **Keyword-based KB search** tool
- **Docker support**
- **Pytest unit tests**
- **Streamlit UI** for demo interface

This project fulfills the complete requirements of the assignment.

---

# 📂 Project Structure

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

---

# 🔧 Installation

## 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

## 2. Install dependencies
pip install -r requirements.txt

## 3. Configure .env file
GEMINI_API_KEY=your_gemini_key
GEMINI_MODEL=gems-1.5-flash

---

# 🚀 Running FastAPI Backend

uvicorn app.main:app --reload --port 8000

### Test endpoints:
- http://localhost:8000/health
- http://localhost:8000/docs

---

# 🖥 Run Streamlit UI

streamlit run ui.py  
Open UI at: http://localhost:8501

---

# 🧪 Run Tests

pytest

---

# 🐳 Docker Run

docker build -t triage-agent .
docker run -p 8000:8000 --env-file .env triage-agent

---

# 🧠 How the Triage Agent Works

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

---

# 🔐 Production Considerations (Required by Assignment)

## 1. Deployment Strategy
For production deployment, the backend would run inside a Docker container on:
- AWS ECS/Fargate  
- Google Cloud Run  
- Azure Container Apps  

This ensures autoscaling, easy rollouts, and stable infrastructure.

---

## 2. Logging & Monitoring
Use structured JSON logs and send them to:
- AWS CloudWatch  
- GCP Cloud Logging  
- Elastic Stack  
- Grafana Loki  

Monitor:
- Latency (P50, P95, P99)
- Error rates (4xx/5xx)
- LLM failures/timeouts
- CPU/RAM usage

Set alerts for high latency or error rates.

---

## 3. Configuration & Secrets
Never commit secrets.

Use:
- AWS Secrets Manager  
- GCP Secret Manager  
- Azure Key Vault  

Load configuration using environment variables (12-factor app).

---

## 4. Latency, Cost & Rate Limiting

### Latency
- Use smaller/faster Gemini models for cheaper inference  
- Cache frequent requests  
- Parallelize LLM + KB calls  

### Cost
- Minimize number of LLM calls  
- Cache similar tickets  
- Use model tiers smartly  

### Rate Limiting
- API gateway throttling  
- Protect LLM quota  
- Prevent abuse  

---

# ✔ End of Submission (As Required)

This submission includes:

- Complete FastAPI backend  
- Gemini LLM ticket processor  
- Knowledge Base (JSON)  
- KB Search Tool  
- Ticket Triage Agent  
- Unit tests  
- Dockerfile  
- Streamlit UI  
- Updated README with Production Considerations  

All requirements from the assignment PDF have been successfully completed.

