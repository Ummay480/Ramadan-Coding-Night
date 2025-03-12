import streamlit as st #for the web app
import random   # for the random questions
import time #for the time delay

#Define the questions and answers in the form of a list of dictionaries
st.title("📝Quiz Application")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the founder of Apple?",
        "options": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Steve Jobs"
    },
    {
        "question": "What is the language of France?",
        "options": ["French", "English", "German", "Spanish"],
        "answer": "French"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Which city is known as the 'City of Love'?",
        "options": ["Paris", "London", "Rome", "Barcelona"],
        "answer": "Paris"
    },    
    {
        "question": "What is the capital of Germany?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Berlin"
    },  

]

#Initialize the session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from the session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio button for the options
selected_option = st.radio("Choose your answer", question["options"])

# Submit the answer
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.error("❌ Incorrect! The correct answer is " + question["answer"])

# Wait for 3 seconds before showing the next question
    time.sleep(3)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the new question
    st.rerun()
