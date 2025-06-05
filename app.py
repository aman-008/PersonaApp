import streamlit as st
from persona import generate_reply

st.set_page_config(page_title="Hitesh Bhai Bot 💬", layout="centered")

st.title("🧠 Chat with Hitesh Bhai Bot")
st.caption("Tech + Motivation in Hinglish – Ask anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hanjii bhai! Kya puchna hai aaj?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input
user_prompt = st.chat_input("Aapka sawaal yahan likhiye...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Get response from persona.py
    with st.spinner("Soch rahe hain..."):
        reply = generate_reply(st.session_state.messages)
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append(
            {"role": "assistant", "content": reply})
