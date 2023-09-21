import requests
from random import sample
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
USER = os.environ.get("USER") 
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

connection = psycopg2.connect(dbname = DB_NAME, user = USER, password = PASSWORD, host = HOST, port = PORT)
cursor = connection.cursor()

url = "https://restcountries.com/v3.1/all"

response = requests.get(url)

data = response.json()
countries = sample(data, 10)

def get_common_name(country):
    name = country.get('name') # returns value OR None
    if name is not None:    
        common_name = name.get('common')
    return common_name

def get_capital(country):
    capital_list = country.get('capital')
    if capital_list is not None:
        capital = capital_list[0]
    return capital

def get_flag(country):
    flag_list = country.get('flags') # returns value OR None
    if flag_list is not None:    
        flag = flag_list["png"]
    return flag.replace('https://', '')

def get_subregion(country):
    subregion_name = country.get('subregion') # returns value OR None
    return subregion_name

def get_population(country):
    population = country.get('population') # returns value OR None
    return population

# print(get_common_name(country))
# print(get_capital(country))
# print(get_flag(country))
# print(get_subregion(country))
# print(get_population(country))
for i in range(10):
    country = countries[i]
    name = get_common_name(country)
    capital = get_capital(country)
    flag = get_flag(country)
    subregion = get_subregion(country)
    population = get_population(country)
    query = f'''
    insert into countries (name, capital, flag, subregion, population)
    values(
    '{name}','{capital}','{flag}','{subregion}','{population}'
    );
    '''
    cursor.execute(query)
    connection.commit()
connection.close()