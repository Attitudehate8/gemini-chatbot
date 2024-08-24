import streamlit as st
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Set up credentials (replace with your credentials file)
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your-service-account-file.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Streamlit app
st.title("ASA Chatbot")

# Instructions
st.write("Ask anything and the ASA chatbot will respond!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    try:
        # Obtain an access token
        credentials.refresh(Request())
        token = credentials.token

        # Make an API request to the Gemini model
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }

        data = {
            'model': 'gemini-3',  # Use the correct model name
            'messages': [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        }

        response = requests.post(
            'https://gemini.googleapis.com/v1/models/gemini-3:generateText',  # Use the correct endpoint
            headers=headers,
            json=data
        )

        result = response.json()
        bot_reply = result['choices'][0]['message']['content']

        # Display the reply
        st.text_area("ASA:", value=bot_reply, height=200)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
