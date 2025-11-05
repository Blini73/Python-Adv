import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("This is a sidebar.")

st.sidebar.selectbox("Choose as option", ["Option 1", "Option 2", "Option 3"])
st.sidebar.radio("Go to", ["Home", "Data", "Settings"])