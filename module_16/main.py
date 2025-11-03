import streamlit as st

if st.button("click me"):
    st.write("button clicked")

if st.checkbox("Check me to show some text"):
    st.write("hello world")

user_input = st.text_input("Enter Text", "Sample text")

st.write("ti e ke shkru:", user_input)


age =st.number_input("Enter your age: ", min_value=0, max_value=100)
st.write(f"Your age is {age}")

message = st.text_area("Enter a text")

st.write(f"Your message is {message}")

choice = st.radio("Pick me ", ["choice 1","Choice 2","choice 3" ])

st.write(f"You chose : {choice}")

if st.button("Success"):
    st.success("Operation was successful")


