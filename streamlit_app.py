import streamlit as st

st.title("My parents new healthy dinner")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)


st.header("Breakfast Menu")
st.text(" 🥣 Soup")
st.text(" 🥗 Kale")
st.text(" 🐔🥣 Chiken soup")
st.text(" 🥑🍞 Avocato toast")
