import streamlit as st
from models import chatInteraction
from models import openaiName

messagesOpen = 'messagesOpenSolo'

# Client settings
st.set_page_config(page_title = 'Montasai')

# Sidebar with system prompt
with st.sidebar:

    st.header('OpenAI Chatbot')
    systemPrompt = st.text_area(
        'System Prompt', 
        value = 'You are a data scientist. You reply with concise statements. Do not write too much.'
    )

if prompt := st.chat_input('Ask the model'):
    st.markdown(openaiName)
    chatInteraction(systemPrompt, openaiName, messagesOpen, prompt)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html = True)