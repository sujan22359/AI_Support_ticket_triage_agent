from fastapi import FastAPI, HTTPException
from .schemas import TriageRequest
from .agent import triage_ticket

app = FastAPI(title="Support Ticket Triage Agent")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/triage", response_model=dict)
async def triage(req: TriageRequest):
    desc = req.description or ""
    if not desc.strip():
        raise HTTPException(status_code=400, detail="description is required")
    result = triage_ticket(desc)
    return result
