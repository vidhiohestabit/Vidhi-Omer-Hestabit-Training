import streamlit as st
from orchestrator.nexus import NexusAI  # correct path based on your structure

st.title("NEXUS AI")

# Init agent and chat history
if "agent" not in st.session_state:
    st.session_state.agent = NexusAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from NexusAI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.run(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})