from dotenv import load_dotenv
import streamlit as st

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatMistralAI(
    model_name="mistral-small-2506",
    temperature=0.8
)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="Be a friendly, humorous AI. Use emojis in every reply and light sarcasm when it fits."
        )
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)

prompt = st.chat_input("Type your message...")

if prompt:
    if prompt == "0":
        st.info("Chat ended 👋")
        st.stop()

    st.session_state.messages.append(HumanMessage(content=prompt)) # type: ignore
    st.session_state.chat_history.append(("user", prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.text)) # type: ignore
    st.session_state.chat_history.append(("assistant", response.text))

    with st.chat_message("assistant"):
        st.markdown(response.text)