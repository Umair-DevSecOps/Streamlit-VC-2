import streamlit as st

st.title("Snowflake Version Control Demo")

st.write("This application is connected to GitHub.")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name}!")

st.divider()

st.subheader("Version Control Test")

st.write("This feature was developed on a separate Git branch.")

st.button("Test Version 2")