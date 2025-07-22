from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
import streamlit as st
import asyncio

set_tracing_disabled(True)
MODEL_NAME = 'gemini-2.5-flash'

client = AsyncOpenAI(
    api_key = st.secrets['GEMINI_API_KEY'],
    base_url = 'https://generativelanguage.googleapis.com/v1beta/openai/'
)

model = OpenAIChatCompletionsModel(
    model = MODEL_NAME,
    openai_client = client
)

agent = Agent(
    name = 'Assistant',
    instructions = 'You are a helpful assistant',
    model = model
)

st.set_page_config('💬 AI Assistant')

st.title('💬 AI Assistant Demo')

st.markdown('Ask aunything and see how the assistant responds in real-time.')

user_input = st.text_input('👤 Your Question:')

if st.button('🚀 Ask Assistant'):
    if user_input.strip() != ' ':
        with st.spinner('🤖 Generating response...'):
            result = asyncio.run(Runner.run(starting_agent = agent, input = user_input))
            st.success('✅ Response generated!')
            st.write(f'**🧠 Assistant:** {result.final_output}')

    else:
        st.warning('❗ Please enter a question.')