from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_triage_endpoint_ok():
    payload = {"description": "Login fails: password reset email not received by user"}
    r = client.post("/triage", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "summary" in data
    assert "category" in data
    assert "kb_matches" in data
    assert "issue_type" in data

def test_triage_empty_description():
    r = client.post("/triage", json={"description": ""})
    assert r.status_code == 400
