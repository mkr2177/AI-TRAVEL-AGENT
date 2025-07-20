import requests
from langchain_core.tools import tool

WEATHER_API_KEY = "e1dce3f7088c640e8cf42b6d4f1fc204"

@tool
def get_weather_data(city: str) -> str:
    """Get current weather for a city."""
    url = f"http://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}"
    res = requests.get(url).json()

    if "current" not in res:
        return "⚠️ Could not retrieve weather."

    w = res["current"]
    return (
        f"🌤️ Temperature: {w['temperature']}°C\n"
        f"💧 Humidity: {w['humidity']}%\n"
        f"🌫️ Condition: {w['weather_descriptions'][0]}\n"
        f"💨 Wind: {w['wind_speed']} km/h {w['wind_dir']}"
    )
