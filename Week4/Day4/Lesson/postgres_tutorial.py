import psycopg2

DB_NAME = "actors"
USER = "postgres" 
PASSWORD = "super98" 
HOST = "localhost"
PORT = "5432" # or 5433

try:
    connection = psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
except Exception as e:
    print(f"Error: {e}")

# 2 Create a cursor object

cursor = connection.cursor()

def create_table(table_name: str): # create new table
    query = f'''
    create table {table_name}(
        id serial primary key,
        num integer not null
    );
    '''

    cursor.execute(query) # execute the query
    connection.commit() # make changes in the database

# create_table("new_table_2")

def insert_into_table (table_name:str, num_value:int):
    query = f'''
    insert into {table_name}(num)
    values
    ({num_value});
    '''
    cursor.execute(query) # execute the query
    connection.commit() # make changes in the database

insert_into_table("new_table",12312)
insert_into_table("new_table",88888)


table_name = 'new_table'
query = f"select * from {table_name};"

cursor.execute(query)
output = cursor.fetchall()
print(output)

connection.close()