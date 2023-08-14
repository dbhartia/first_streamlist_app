import streamlit
streamlit.title('My Parents New Healthy Driver')
streamlit.header('🥣 Breakfast Favorites')
streamlit.text(' 🥗  Kale, Spinach & rocket Smoothie')
streamlit.text(' 🐔   Hard-Boiled Free-Range Egg')
streamlit.text('  🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.pandas(my_fruit_list);

