import streamlit as st
import random

st.title('Multiplication Quiz')
st.sidebar.title('Options')
num_questions = st.sidebar.slider('Number of Questions', 1, 10, 5)

# Display a random multiplication question and ask the user to input the correct answer
correct_answers = 0
for i in range(num_questions):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    user_answer = st.number_input(f'Question {i+1}: {num1} x {num2} =', min_value=0, max_value=100, step=1)
    if user_answer == correct_answer:
        st.write('Correct!')
        correct_answers += 1
    else:
        st.write(f'Sorry, the correct answer was {correct_answer}.')

# Display the user's score
st.write(f'You got {correct_answers} out of {num_questions} questions correct.')

$ streamlit run streamlit_app.py

