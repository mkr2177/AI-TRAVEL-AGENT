from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def get_places_to_visit(city: str) -> str:
    """Returns top tourist places using DuckDuckGo."""
    query = f"Top tourist places in {city}"
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        return "📍 Places to Visit:\n" + "\n".join([f"• {r['body']}" for r in results])
