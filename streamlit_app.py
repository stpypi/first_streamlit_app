# Created the main python file.

import streamlit 
import pandas

streamlit.title("My parents new healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text(" 🥣 Idly Sambar")
streamlit.text(" 🥗 Poha")
streamlit.text(" 🥑 Sandwitch")
streamlit.text(" 🍞 Oat Milk")
streamlit.text(" 🐔 Hard-Boiled Free-Range Egg ")

   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
