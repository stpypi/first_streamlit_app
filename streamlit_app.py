# Created the main python file.

import streamlit 
import pandas
import requests

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

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruits they  want to include 
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Lime','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display selected fruits 
streamlit.dataframe(fruits_to_show)

#display the table on the page 
streamlit.dataframe(my_fruit_list)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())
# normalize the json version of the response 
# pandas converts the json into the data frame a tabular format to display
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# and streamlit displays the data from the fruityvice_normalized variable. 
streamlit.dataframe(fruityvice_normalized)
