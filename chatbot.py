import streamlit as st
import json

# Load intents from the JSON file
with open("dataset.json", "r") as file:
    data = json.load(file)

# Function to find best matching intent
def get_bot_response(user_message):
    user_message = user_message.lower()
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_message:
                return random.choice(intent["responses"])
    return "I'm not sure how to respond, but I'm here to listen."

# Streamlit app setup
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Chatbot")
st.markdown("Hi I am Luma. Tell me how you're feeling. I'm here to support you. 💬")

# User input
user_input = st.text_input("You:", placeholder="How are you feeling today?")

# Bot response
if user_input:
    import random
    bot_reply = get_bot_response(user_input)
    st.markdown(f"**Bot:** {bot_reply}")
