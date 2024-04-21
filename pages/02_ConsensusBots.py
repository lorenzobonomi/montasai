import streamlit as st
from models import chatInteraction
from models import anthropicName, openaiName, messagesAnt, messagesOpen

st.set_page_config(page_title = 'Montasai')
st.sidebar.header("Montasai")

promptConsensus = ''
promptTest1, promptTest2 = None, None

with st.sidebar:

    st.header('ConsensusBots')

    st.markdown('#### System Prompt')
    systemPrompt = st.text_area(
        '', 
        value = 'You are a data scientist. You reply with concise statements. Do not write too much.'
    )

    st.markdown('***')
    st.markdown('#### Choose Consensus Iterations')
    numberConsensus = st.slider('', min_value = 1, max_value = 5, value = 1, step = 1)
    
    st.markdown('#### Activate Consensus')
    on = st.toggle('')

 
col1, col2 = st.columns(2)

if prompt := st.chat_input('Ask the models'):

    with col1:
        st.markdown(anthropicName)
        risposta = chatInteraction(systemPrompt, anthropicName, messagesAnt, prompt)
        st.session_state['rispostaAnt1'] = risposta

    with col2:
        st.markdown(openaiName)
        risposta = chatInteraction(systemPrompt, openaiName, messagesOpen, prompt)
        st.session_state['rispostaOpen1'] = risposta

elif on:
    st.write('Consensus activated!')
    promptConsensus = [
        'I asked the same question to another model. Please analyze its answer in [] and improve your answer',
        'I asked to evaluate your second answers to the other model. Please analyze its answer in [] and improve your answer',
        'I asked again to evaluate your answers to the other model. Please analyze its answer in [] and improve your answer'
    ]

    for i in range(1, numberConsensus + 1):

        with col1:
            st.markdown(anthropicName)
            agg = st.session_state[f'rispostaOpen{i}']
            promptConsensusAnt = promptConsensus[i-1] + f'[{agg}]'

            risposta = chatInteraction(systemPrompt, anthropicName, messagesAnt, promptConsensusAnt)
            st.session_state[f'rispostaAnt{i + 1}'] = risposta

        with col2:
            st.markdown(openaiName)
            agg = st.session_state[f'rispostaAnt{i}']
            promptConsensusOpen = promptConsensus[i-1] + f'[{agg}]'
            risposta = chatInteraction(systemPrompt, openaiName, messagesOpen, promptConsensusOpen)
            st.session_state[f'rispostaOpen{i + 1}'] = risposta