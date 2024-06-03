import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
API_URL =os.getenv('API_URL')

def response(text):
    resp = requests.post(f"{API_URL}/resposta/", json={"text": text})
    return resp.json()



# STREAMLIT
st.title("Bot Maria Saúde")


if "messages" not in st.session_state.keys():
    st.session_state.messages=[
        {"role":"assistant","content": "Olá, como posso ajudar?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role":"user","content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = response(user_prompt)
            st.write(ai_response['text'])
    new_ai_message = {"role":"assistant","content": ai_response['text']}
    st.session_state.messages.append(new_ai_message)
