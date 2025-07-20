# 🧳 AI Travel Assistant

An intelligent **AI Travel Agent** built using **LangChain**, **Streamlit**, and real-world APIs like WeatherStack, Serper.dev, and DuckDuckGo Search.

This assistant acts like a real travel agent — answering natural language queries, planning your itinerary, finding hotels, weather conditions, and tourist attractions — all in one place.

---

## 🤖 How It Works

This app uses a **LangChain Agent** (LLM-powered) that:
- Understands your intent from plain English
- Decides which tools to use (weather, search, hotels)
- Gathers data in real time
- Returns a clean and structured response like a human travel agent

---

## 🚀 Features

- 🌦️ Live weather updates (via WeatherStack)
- 🏨 Hotel recommendations (via Serper.dev + Google)
- 📍 Top tourist attractions (via DuckDuckGo)
- 📜 Past trip history (stored locally)
- 🧠 Smart agent logic (using LangChain Zero-Shot Agent)
- 🗣️ Natural language interaction

---

## 🛠️ Tech Stack

| Component    | Tool/API Used            |
|--------------|---------------------------|
| LLM Agent     | Groq (LLaMA 3 via LangChain) |
| UI           | Streamlit                 |
| Weather      | WeatherStack API          |
| Hotels       | Serper.dev API            |
| Search       | DuckDuckGo Search API     |
| Memory       | Local JSON storage        |
