import json
import re
import google.generativeai as genai
from .config import GEMINI_API_KEY, GEMINI_MODEL


if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def _clean_model_text(text: str) -> str:
    """Remove markdown fences and surrounding text so JSON can be parsed."""
    if not text:
        return ""
    
    text = re.sub(r"```(?:json)?", "", text)
    return text.strip()

def gemini_extract(description: str) -> dict:
    """
    Call Gemini to extract structured fields from a ticket description.
    Returns a dict: {summary, category, severity, suggested_next_steps, clarifying_questions}
    """
    prompt = f"""
You are a support-ticket triage assistant. Read the user ticket below and return ONLY valid JSON (no extra commentary).

Ticket:
\"\"\"{description}\"\"\"

Return JSON with the following keys:
- summary: short 1-2 line summary (string)
- category: one of [Billing, Login, Performance, Bug, Notification, User Profile, Sync, Question/How-To]
- severity: one of [Low, Medium, High, Critical]
- suggested_next_steps: short instruction for the support team (string)
- clarifying_questions: array of strings; empty array if none
"""

    model = genai.GenerativeModel(GEMINI_MODEL)
    try:
        resp = model.generate_content(prompt)
        text = _clean_model_text(resp.text)
        
        try:
            return json.loads(text)
        except Exception:
            
            m = re.search(r"(\{[\s\S]*\})", text)
            if m:
                return json.loads(m.group(1))
            
            return {
                "summary": (description[:200] + "...") if len(description) > 200 else description,
                "category": "Question/How-To",
                "severity": "Medium",
                "suggested_next_steps": "Investigate manually",
                "clarifying_questions": []
            }
    except Exception as e:
        
        return {
            "summary": (description[:200] + "...") if len(description) > 200 else description,
            "category": "Question/How-To",
            "severity": "Medium",
            "suggested_next_steps": "Investigate manually",
            "clarifying_questions": [f"LLM error: {str(e)}"]
        }
