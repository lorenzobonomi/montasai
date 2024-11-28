import streamlit as st
from models import chatInteraction
from models import openaiName

messagesAnt = 'messagesOpenAI01Solo'
#odelversion = 'o1-preview-2024-09-12'

st.set_page_config(page_title = 'Montasai')
st.sidebar.header("Montasai")

with st.sidebar:
    st.header('OpenAI01')
    systemPrompt = st.text_area(
        'System Prompt', 
        value = 'You are a data scientist. You reply with concise statements. Do not write too much.'
    )

    optionLatex = st.radio("Enable LatexFormatting:", ("Yes", "No"))

if prompt := st.chat_input('Ask the model'):
    st.markdown(openaiName)

    if optionLatex == "Yes":
        prompt = prompt + st.session_state.latexFormatting

    chatInteraction(systemPrompt, openaiName, messagesAnt, prompt, st.session_state.modelversionOAI01)



