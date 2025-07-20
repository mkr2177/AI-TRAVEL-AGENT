import streamlit as st
from agents.travel_agent import agent_executor
from utils.history import save_trip, load_history

st.set_page_config(page_title="AI Travel Assistant", page_icon="🧳")
st.title("🧳 AI Travel Assistant")

st.markdown("""
Ask anything like:
- "Plan a weekend trip to Gaya"
- "What's the weather and good hotels in Manali?"
""")
# ✍️ Text Input Only
query = st.text_input("Type your travel query:", placeholder="e.g., Plan 2 days in Gaya")

# 🧠 Process Query
if st.button("Plan Now") and query:
    with st.spinner("Generating your travel plan..."):
        try:
            response = agent_executor.invoke({"input": query})
            st.markdown("### 🗺️ Trip Plan")
            st.markdown(response["output"])
            save_trip(query, response["output"])
        except Exception as e:
            st.error(f"❌ Failed to generate plan: {e}")

# 📜 Trip History
with st.expander("📜 Show Past Trips"):
    for trip in reversed(load_history()):
        st.markdown(f"**🕒 {trip['timestamp']}**\n\n**Query**: {trip['query']}\n\n{trip['response']}\n---")
