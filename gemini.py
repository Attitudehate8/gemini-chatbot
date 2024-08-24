import openai
import streamlit as st

# Set up the OpenAI API client
openai.api_key = "AIzaSyBxC7YYFatIpC6iM25K7MOhZDn-Ojkaud0"

# Streamlit app
st.title("ASA Chatbot")

# Instructions
st.write("Ask anything and the ASA chatbot will respond!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Make a request to the Gemini API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )

    # Extract the chatbot's reply
    bot_reply = response.choices[0].message['content']

    # Display the reply
    st.text_area("ASA:", value=bot_reply, height=200)
