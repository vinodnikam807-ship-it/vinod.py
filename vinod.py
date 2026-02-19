import streamlit as st

from demofile import button

st.title ("Welcome to Vinod Nikam")
st.markdown("<h1 style='color:green;'>Vinod</h1>", unsafe_allow_html=True)
st.header ("Enter of name")
name = st.text_input("Enter the name: ")
fname = st.text_input("Enter the surname")
button = st.button ("print")
