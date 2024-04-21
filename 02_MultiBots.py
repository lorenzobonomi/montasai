
import streamlit as st
from models import chatInteraction
from models import anthropicName, openaiName, messagesAnt, messagesOpen

st.set_page_config(page_title = 'Montasai')
st.sidebar.header("Montasai")

with st.sidebar:

    st.header('MultiBots')
    systemPrompt = st.text_area(
        'System Prompt', 
        value = 'You are a data scientist. You reply with concise statements. Do not write too much.'
    )
    
col1, col2 = st.columns(2)

if prompt := st.chat_input('Ask the models'):

    with col1:
        st.markdown(anthropicName)
        chatInteraction(systemPrompt, anthropicName, messagesAnt, prompt)

    with col2:
        st.markdown(openaiName)
        chatInteraction(systemPrompt, openaiName, messagesOpen, prompt)


        



