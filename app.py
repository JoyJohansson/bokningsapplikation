from flask import Flask, render_template, request
from psycopg2 import connect, DatabaseError, pool
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Set up a connection pool
db_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
)

def execute_query(query, parameter=None, fetch_result=False):
    connection = None
    try:
        connection = db_pool.getconn()
        with connection, connection.cursor() as cursor:
            cursor.execute(query, parameter)
            connection.commit()
            if fetch_result:
                return cursor.fetchall()
            else:
                 return cursor.rowcount > 0
             
    except DatabaseError as error:
        return str(error)
    finally:
        if connection:
            db_pool.putconn(connection)


query = "SELECT * FROM hotel"
hotels = execute_query(query, fetch_result=True)
if isinstance(hotels, list):
        print("Query executed successfully.")
        for hotel in hotels:
            print(hotel)
else:
        print("Error executing query.")

if __name__ == "__main__":
    app.run(debug=True)
    

