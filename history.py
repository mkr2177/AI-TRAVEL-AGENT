import json
from datetime import datetime

def save_trip(query, response):
    history = load_history()
    history.append({
        "query": query,
        "response": response,
        "timestamp": str(datetime.now())
    })
    with open("trip_history.json", "w") as f:
        json.dump(history, f, indent=2)

def load_history():
    try:
        with open("trip_history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
