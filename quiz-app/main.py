# I built a Quiz App using Python and Streamlit that lets users test their knowledge with multiple-choice questions

import streamlit as st
import random
import time


# Set the title of the app
st.title("Quiz Application")

# List of quiz questions with options and correct answer
questions = [
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "What is the result of print(5 > 3)?",
        "options": ["True", "False", "5", "Error"],
        "answer": "True"
    },
    {
        "question": "Which function is used to get the input from the user?",
        "options": ["input()", "print()", "scan()", "input_text()"],
        "answer": "input()"
    },
    {
        "question": "How do you create a variable in Python?",
        "options": ["x = 5", "let x = 5", "var x = 5", "x := 5"],
        "answer": "x = 5"
    },
    {
        "question": "Which of the following is the correct syntax to create a list?",
        "options": ["[]", "()", "{}", "<>"],
        "answer": "[]"
    },
    {
        "question": "Which of the following is a Python data type?",
        "options": ["integer", "int", "number", "float64"],
        "answer": "int"
    },
    {
        "question": "Which of the following is used to add an item to a list in Python?",
        "options": ["add()", "append()", "insert()", "extend()"],
        "answer": "append()"
    },
    {
        "question": "How do you define a function in Python?",
        "options": ["function my_func()", "def my_func()", "func my_func()", "define my_func()"],
        "answer": "def my_func()"
    },
    {
        "question": "What is the data type of True?",
        "options": ["bool", "int", "str", "float"],
        "answer": "bool"
    },
    {
        "question": "Which of the following is used to define a dictionary in Python?",
        "options": ["[]", "{}", "()", "<>"],
        "answer": "{}"
    },
]

# Check if session state for current question exists, if not, initialize it
if "current_questions" not in st.session_state:
    st.session_state.current_questions = random.choice(questions)

# Get the current question
question = st.session_state.current_questions

st.subheader(question["question"])

# Radio button for selecting an option
selected_option = st.radio("Select an option", question["options"],key= "answer")

# submit button
if st.button("submit answer"):
    if selected_option == question["answer"]:
        st.success("Correct Answer!")
        st.balloons()
    else:
        st.error("Wrong Answer! the correct answeris " + question["answer"])
    # Wait for 3 seconds before showing the next question
    time.sleep(3)    
    st.session_state.current_questions = random.choice(questions)
    st.rerun()



