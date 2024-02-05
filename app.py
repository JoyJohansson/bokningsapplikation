from flask import Flask, render_template, request, redirect, url_for
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
            

@app.route("/", methods=["GET"])
def k1():
    query = "SELECT * FROM K2"
    results = execute_query(query, fetch_result=True)
    
    if results:
        return render_template("k1.html", results=results)
    else:
        return render_template("k1.html", error="hejdå")


@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/K2", methods=["POST"])
def k2():
    guests = request.form.get("guests")
    error = "För stort sällskap"
    query = "SELECT * FROM K2"
    result = execute_query(query,fetch_result=True)
    print(result)
    if result:
        return render_template("k2_available_rooms.html", result=result)
    else:
        return render_template("k1.html",error=error)    

if __name__ == "__main__":
    app.run(debug=True)

