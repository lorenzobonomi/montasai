import streamlit as st
import anthropic
from openai import OpenAI

anthropicName = 'Anthropic'
openaiName = 'OpenAI'
messagesAnt = 'messages' + anthropicName
messagesOpen = 'messages' + openaiName
anthropicKey = 'ANTHROPIC_API_KEY'
openaiKey = 'OPENAI_API_KEY'


class ModelAnthropic:

    def __init__(self, temperature, system, maxTokens, modelversion):

        self.model = modelversion
        self.temperature = temperature
        self.system = system
        self.max_tokens = maxTokens
        self.client = anthropic.Anthropic(
            api_key = st.secrets[anthropicKey]
        )
        self.systemPrompt = system


    def createM(self, messagesAnt):
        
        stream = self.client.messages.create(
                model = self.model,
                system = self.system,
                messages = [
                    {'role': m['role'], 'content': m['content']}
                    for m in messagesAnt
                ],
                max_tokens = self.max_tokens,
            )
        return stream
    

class ModelOpenAI:

    def __init__(self, temperature, modelversion, reasoningEffort):

        self.model = modelversion
        self.temperature = temperature
        self.client = OpenAI(api_key = st.secrets[openaiKey])
        self.reasoningEffort = reasoningEffort

    def createM(self, messagesOpenAI):
        
        stream = self.client.chat.completions.create(
                model = self.model,
                messages = [
                    {'role': m['role'], 'content': m['content']}
                    for m in messagesOpenAI
                ],
                stream = True,
            )

        return stream
    

    
def chatInput(messagesName, client, modelName, prompt):

    if messagesName not in st.session_state:
        st.session_state[messagesName] = []

    if modelName not in st.session_state:
        st.session_state[modelName] = client.model

    for message in st.session_state[messagesName]:
        with st.chat_message(message['role']):
            if message['role'] == 'user' or modelName == openaiName:
                st.markdown(message['content'])   
            else:
                st.markdown(message['content'][0].text)
    
    st.session_state[messagesName].append({'role': 'user', 'content': prompt})

    with st.chat_message('user'):
        st.markdown(prompt)


def chatOutput(modelName, messagesName, systemPrompt, client, modelversion):

    if modelName == openaiName:
        with st.chat_message('assistant'):
            if modelversion == 'gpt-4o':
                st.session_state[messagesName].append({'role': 'system', 'content' : systemPrompt})
            stream = client.createM(st.session_state[messagesName])
            response = st.write_stream(stream)

        st.session_state[messagesName].append({'role': 'assistant', 'content': response})

        return response

    else:
        with st.chat_message('assistant'):
            stream = client.createM(st.session_state[messagesName])
            st.write(stream.content[0].text)

        st.session_state[messagesName].append({'role': 'assistant', 'content': stream.content})

        return stream.content[0].text


def chatInteraction(systemPrompt, modelName, messagesName, prompt, modelversion, reasoningEffort):
    
    consensus = "I asked the same question to another model. Please analyze its answer in [] and improve your answer"

    if modelName == openaiName:
        client = ModelOpenAI(0, modelversion, reasoningEffort)
    else:
        client = ModelAnthropic(0, systemPrompt, 500, modelversion)
    
    chatInput(messagesName, client, modelName, prompt)
    risposta = chatOutput(modelName, messagesName, systemPrompt, client, modelversion)

    return risposta

        