from pydantic import BaseModel
from typing import List, Optional


class TriageRequest(BaseModel):
    description: str


class KBMatch(BaseModel):
    id: str
    title: str
    score: float
    recommended_action: str


class TriageResponse(BaseModel):
    summary: str
    category: str
    severity: str
    kb_matches: List[KBMatch]
    issue_type: str # "known_issue" or "new_issue"
    suggested_action: str
    clarifying_questions: Optional[List[str]] = []