import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

# Get connection from snowflake
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = 


def get_fruit_information(fruit_choice):
    # Info from fruity vice
    fruityvice_response = requests.get(
        "https://fruityvice.com/api/fruit/" + fruit_choice
    )
    # normalize json into a dataframe
    return pd.json_normalize(fruityvice_response.json())

def get_fruit_list():
    with my_cnx.cursor() as my_cur:
        # Get fruits
        my_cur.execute("SELECT fruit_name as fruit from pc_rivery_db.public.fruit_load_list;")
        my_list_of_fruits = list(my_cur.fetchall())
        return my_list_of_fruits

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
try:
    # Pick some fruit + add button
    container1 = st.container()
    fruit_choice = container1.text_input(
        "What fruit would you like information about?", "Kiwi"
    )
    container2 = st.container()
    add_button = container2.button("add")
    if not fruit_choice:
        st.error("Please select a fruit to get information")
    else:
        # Get and normalize data from fruit
        fruityvice_normalized = get_fruit_information(fruit_choice)
        # Display the dataframe in streamlit
        st.dataframe(fruityvice_normalized)

except URLError as e:
    st.error()


# if add_button:
#     my_list_of_fruits.append("".join(fruit_choice))

# Fruit list from snowflake
st.header("The list of fruits contains:")
if st.button('Click to load information'):
    my_list_of_fruits = get_fruit_information()
    st.dataframe(my_list_of_fruits)
