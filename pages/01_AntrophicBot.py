import streamlit as st
from models import chatInteraction
from models import anthropicName

messagesAnt = 'messagesAntSolo'

st.set_page_config(page_title = 'Montasai')
st.sidebar.header("Montasai")

with st.sidebar:
    st.header('AnthropicBot')
    systemPrompt = st.text_area(
        'System Prompt', 
        value = 'You are a data scientist. You reply with concise statements. Do not write too much.'
    )

if prompt := st.chat_input('Ask the model'):
    st.markdown(anthropicName)
    chatInteraction(systemPrompt, anthropicName, messagesAnt, prompt)


