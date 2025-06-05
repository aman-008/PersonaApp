import streamlit as st
from persona import generate_reply

st.set_page_config(page_title="Hitesh Bhai Bot 💬", layout="centered")

# Password Protection
PASSWORD = st.secrets["app_password"]

def check_password():
    def password_entered():
        if st.session_state["password"] == PASSWORD:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        st.error("Incorrect password")
        return False
    else:
        return True

# Main App
if check_password():
    st.title("🧠 Chat with Hitesh Bhai Bot")
    st.caption("Tech + Motivation in Hinglish – Ask anything!")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hanjii bhai! Kya puchna hai aaj?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    user_prompt = st.chat_input("Aapka sawaal yahan likhiye...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.spinner("Soch rahe hain..."):
            reply = generate_reply(st.session_state.messages)
            st.chat_message("assistant").markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
