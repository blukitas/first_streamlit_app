import streamlit as st
import pandas as pd
import requests
import snowflake.connector

my_fruit_list = pd.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
)

st.title("My parents new healthy dinner")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)


st.header("Breakfast Menu")
st.text(" 🥣 Soup")
st.text(" 🥗 Kale")
st.text(" 🐔🥣 Chiken soup")
st.text(" 🥑🍞 Avocato toast")

# Change index to name
my_fruit_list = my_fruit_list.set_index("Fruit")

# Display a multiselect with fruits index
selected_fruits = st.multiselect(
    "Pick some fruits:", list(my_fruit_list.index), ["Apple", "Lemon", "Avocado"]
)

# Display the dataset
st.dataframe(my_fruit_list.loc[selected_fruits])

# New header
st.header("Fruityvice Fruit Advice!")

# Pick some fruit
fruit_choice = st.text_input("What fruit would you like information about?", "Kiwi")
st.write("The user entered ", fruit_choice)

# Info from fruity vice
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
st.text(fruityvice_response.json())

# normalize json into a dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Display the dataframe in streamlit
st.dataframe(fruityvice_normalized)
