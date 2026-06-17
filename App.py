import streamlit as st
import random

st.title("My Cooking Buddy")
st.subheader("My first AI app")
st.write("Welcome Future Chefs!")
st.write("This app will become a chatbot")
st.title("My Cooking Buddy")
name = st.text_input("Enter your name")
age = st.text_input("Enter your age")
recipe = st.text_input("Enter your recipe")
st.write("Today's goal is to cook",recipe)
if st.button("Start"):
    if not recipe:
        st.error("Please enter your name")
    else:
        st.write("Hello,",name)
        st.write("Ready to cook today?")


recipe = st.selectbox("Choose Recipe", {"Fast food","Healthy Meal","Yummy Desert","Quick Snack"})

if st.button("Plan"):
    if recipe == "Fast food":
         st.write("Make a Fast Food")
    elif recipe == "Healthy Meal":
        st.write("Make a Healthy Meal")
    if recipe == "Yummy Desert":
        st.write("Make a Yummy Desert")
    if recipe == "Quick Snack":
        st.write("Make a Quick Snack")
    else: st.write("Make a Meal")

st.success("Good Luck!")
st.title("Mood Coach")
Mood = ["Sad", "Tired","Okay", "Happy" "Excited"]
Sentence = "How are you feeling today?"
Mood = st.radio(Sentence, Mood)
if st.button("Yes"):
    if Mood == "Sad":
        st.success("Are you okay?")
    elif Mood == "Tired":
        st.success("Let's take a rest")
    if Mood == "Okay":
        st.success("That's good!")
    if Mood == "Happy":
        st.success("YAY! You are happy")
    if Mood == "Excited":
        st.success("YAY! You are excited")

import random
st.title("Motivational Chatbot")
quotes = [
    "Keep going!",
    "You can do it!",
    "Believe in yourself!",
    "You are doing great!",
    "Don't give up!",
    "Every step counts!",
    "You did so well!"]

def bot_reply(text):
    text = text.lower()
    if "tired" in text or 'stressed' in text:
        replies = [
            "You don't need to rush!"
            "You can always do it later!"
            "Take a deep breath first!"
        ]
        return random.choice(replies)

    else:
        replies = [
         "You can do it",
         "Keep trying!",
         "You can do it",
         "Believe in yourself."
        ]
        return random.choice(replies)

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
         st.write(message["content"])
msg = st.chat_input("Ask me anything")

if msg:
    st.session_state.messages.append({"role": "user", "content": msg})
    reply = bot_reply(msg)
    st.session_state.messages.append({"role": "ai", "content": reply})
    st.rerun()
