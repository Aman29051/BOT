import streamlit as st
from instabot import Bot

def send_messages(username, password, target_username, message):
    bot = Bot()
    if bot.login(username=username, password=password):
        followers = bot.get_user_followers(target_username)

        for follower in followers:
            user_id = bot.get_user_id_from_username(follower)
            bot.send_message(message, user_id)

        bot.logout()
        st.success("Messages sent successfully!")
    else:
        st.error("Login failed. Please check your credentials.")

st.title("Instagram DM Bot")

# Input fields
username = st.text_input("Instagram Username")
password = st.text_input("Instagram Password", type="password")
target_username = st.text_input("Target Account Username")
message = st.text_input("Message")

# Button to send messages
if st.button("Send Messages"):
    send_messages(username, password, target_username, message)
