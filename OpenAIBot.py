import streamlit as st
from models import chatInteraction
from models import openaiName

# Define session level variables
if 'modelversionOAI' not in st.session_state or 'modelversionOAI01' not in st.session_state or 'modelversionAnt' not in st.session_state:
    st.session_state.modelversionOAI = 'gpt-4o'
    st.session_state.modelversionOAI01 = 'o1-preview-2024-09-12'
    st.session_state.modelversionAnt = 'claude-3-5-sonnet-20241022'

if 'latexFormatting' not in st.session_state:
    st.session_state.latexFormatting = " wrap latex code with $$"

messagesOpen = 'messagesOpenSolo'

# Client settings
st.set_page_config(page_title = 'Montasai')
st.sidebar.header("Montasai")

# Sidebar with system prompt
with st.sidebar:

    st.header('OpenAIBot')
    systemPrompt = st.text_area(
        'System Prompt', 
        value = 'You are a data scientist. You reply with concise statements.'
    )

    optionLatex = st.radio("Enable LatexFormatting:", ("Yes", "No"))
    

if prompt := st.chat_input('Ask the model'):
    st.markdown(openaiName)

    if optionLatex == "Yes":
        prompt = prompt + st.session_state.latexFormatting

    chatInteraction(systemPrompt, openaiName, messagesOpen, prompt, st.session_state.modelversionOAI, 'low')

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html = True)