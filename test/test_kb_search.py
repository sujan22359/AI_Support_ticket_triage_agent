from app.kb_search import search_kb

def test_kb_search_basic():
    matches = search_kb("Checkout shows 500 error on mobile during payment")
    assert isinstance(matches, list)
    assert len(matches) <= 3
    if matches:
        top = matches[0]
        assert "id" in top and "score" in top and "recommended_action" in top
