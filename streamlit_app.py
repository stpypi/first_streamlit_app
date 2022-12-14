# Created the main python file.

import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


#streamlit.write('The user entered ', fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)       
   # pandas converts the json into the data frame a tabular format to display
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice: 
    streamlit.error("Please select a fruit to get information")
   else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)  
except URLError as e: 
  streamlit.error()

#streamlit.text(fruityvice_response.json())
# normalize the json version of the response 
# and streamlit displays the data from the fruityvice_normalized variable. 

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.text("Hellow from Snowflake : ")
streamlit.header("View Our Fruit List - Add your Favorites!")

#snowflake related function. 
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()
      
# Add a button to laod the fruits 
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
   my_data_rows =  get_fruit_load_list() 
   #streamlit.text(my_data_rows)
   streamlit.dataframe(my_data_rows)
   my_cnx.close()

#streamlit.stop()
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")
      return "Thanks for adding a new fruit "+new_fruit

fruit_to_add = streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
   back_from_function = insert_row_snowflake(fruit_to_add)
   streamlit.text(back_from_function)
   my_cnx.close()
