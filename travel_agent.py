from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI

from tools.weather import get_weather_data
from tools.travel import get_hotels
from tools.search_places import get_places_to_visit

llm = ChatOpenAI(
    model="llama3-8b-8192",
    openai_api_key="YOUR API KEY",
    openai_api_base="https://api.groq.com/openai/v1"
)

tools = [get_weather_data, get_hotels, get_places_to_visit]

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
