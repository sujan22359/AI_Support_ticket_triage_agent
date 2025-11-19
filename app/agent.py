from .kb_search import search_kb
from .llm_client import gemini_extract

# Threshold for deciding a KB match (tune if needed)
KB_MATCH_THRESHOLD = 0.40

def triage_ticket(description: str) -> dict:
    """
    Orchestrate extraction (LLM) + KB search to produce a structured triage result.
    """
    # 1. Extract structured fields using Gemini
    extract = gemini_extract(description)

    # 2. Search KB
    kb_matches = search_kb(description, top_k=3)

    # 3. Decide known/new issue
    top_score = kb_matches[0]["score"] if kb_matches else 0.0

    if top_score > KB_MATCH_THRESHOLD:
        issue_type = "known_issue"
        suggested_action = kb_matches[0]["recommended_action"] or extract.get("suggested_next_steps", "")
    else:
        issue_type = "new_issue"
        suggested_action = extract.get("suggested_next_steps", "Investigate manually")

    return {
        "summary": extract.get("summary", ""),
        "category": extract.get("category", "Question/How-To"),
        "severity": extract.get("severity", "Medium"),
        "kb_matches": kb_matches,
        "issue_type": issue_type,
        "suggested_action": suggested_action,
        "clarifying_questions": extract.get("clarifying_questions", [])
    }
