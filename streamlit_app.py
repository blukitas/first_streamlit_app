import streamlit as st
import pandas as pd

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
