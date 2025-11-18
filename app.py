# app.py
import streamlit as st
from components.ui import header, footer
from components.budget import upload_transactions, show_summary
from granite_pipeline import get_generator
from utils import detect_user_demographic




def main():
header()


st.sidebar.title("Settings")
profile = {}
profile['name'] = st.sidebar.text_input('Name', '')
profile['age'] = st.sidebar.number_input('Age', min_value=0, max_value=120, value=30)
profile['occupation'] = st.sidebar.text_input('Occupation', '')
user_type = detect_user_demographic(profile)
st.sidebar.write("Detected user type:", user_type)


page = st.sidebar.radio('Page', ['Chat', 'Budget', 'Insights', 'Settings'])


# instantiate generator
generator = get_generator()


if page == 'Chat':
st.header('Chat with Finance Bot')
prompt = st.text_area('Ask your question', height=150)
tone = st.selectbox('Tone level', ['Simple (student)', 'Professional (detailed)'])
if st.button('Send'):
with st.spinner('Generating...'):
adapted_prompt = f"UserType: {user_type}\nTone: {tone}\nQuestion: {prompt}\nRespond with actionable personal finance advice."
answer = generator.generate(adapted_prompt, max_new_tokens=400)
st.markdown('**Bot:**')
st.write(answer)


elif page == 'Budget':
df = upload_transactions()
if st.button('Generate Budget Summary'):
show_summary(df)


elif page == 'Insights':
st.header('Spending Insights')
st.info('This page will aggregate trends from uploaded transactions and chat history to offer suggestions.')
if st.button('Run Insights (demo)'):
demo_prompt = ("You are a financial coach. Given a sample user with mixed spending, produce 5 suggestions to reduce non-essential spending and 3 saving goals.")
out = generator.generate(demo_prompt, max_new_tokens=300)
st.write(out)


else:
st.header('Settings')
st.markdown('Manage API keys, model settings, and environment variables here.')


footer()


if __name__ == '__main__':
main()