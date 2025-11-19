import json
import re
from typing import List, Dict
from pathlib import Path

KB_PATH = Path(__file__).resolve().parents[1] / "kb" / "knowledge_base.json"

def load_kb() -> List[Dict]:
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _token_set(text: str):
    return set(re.findall(r"\w+", text.lower()))

def score_match(description: str, kb_entry: Dict) -> float:
    """
    Simple overlap score between ticket description tokens and KB title+symptoms tokens.
    Returns a float score in [0,1].
    """
    desc_tokens = _token_set(description)
    keywords = set()
    keywords.update(_token_set(kb_entry.get("title", "")))
    for s in kb_entry.get("symptoms", []):
        keywords.update(_token_set(s))
    if not keywords:
        return 0.0
    overlap = desc_tokens.intersection(keywords)
    return len(overlap) / max(1, len(keywords))

def search_kb(description: str, top_k: int = 3) -> List[Dict]:
    """
    Return top_k KB matches as a list of dicts: {id, title, score, recommended_action}
    """
    kb = load_kb()
    scored = []
    for entry in kb:
        s = score_match(description, entry)
        scored.append((s, entry))
    scored.sort(reverse=True, key=lambda x: x[0])
    results = []
    for score, entry in scored[:top_k]:
        results.append({
            "id": entry["id"],
            "title": entry["title"],
            "score": float(score),
            "recommended_action": entry.get("recommended_action", "")
        })
    return results
