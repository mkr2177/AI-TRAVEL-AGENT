import requests
from langchain_core.tools import tool

SERPER_API_KEY = "YOUR API KEY"

@tool
def get_hotels(city: str) -> str:
    """Search for hotels using Google via Serper.dev."""
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    data = {"q": f"best hotels in {city}"}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return "⚠️ Failed to fetch hotel data."

    results = response.json().get("organic", [])[:5]
    if not results:
        return "⚠️ No hotels found."

    return "🏨 Hotels:\n" + "\n".join(
        [f"• {h.get('title')}\n  {h.get('snippet')}\n  🔗 {h.get('link')}" for h in results]
    )
