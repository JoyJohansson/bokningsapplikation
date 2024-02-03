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
            

@app.route("/")
def k1():
    return render_template("k1.html")

@app.route("/error")
def error():
    return render_template("error.html")

<<<<<<< HEAD
@app.route("/room_info", methods=["GET"])
def room_info():
    args = request.args
    room_id = args["room_id"]
    query = "SELECT * FROM room WHERE room_id = %s"
    room = execute_query(query, (room_id,))
    return render_template("k3.html", room=room)

@app.route("/book?start_date&end_date&room_id", methods=["POST"])
def book_room(start_date, end_date, room_id):

    query = "INSERT INTO booking(start_date, end_date, room_id) VALUES (%s, %s, %s)"
    success = execute_query(query, (start_date, end_date, room_id))

    if success:
        print("Query executed successfully.")
    else:
        print("Error executing query.")

    return render_template("k4.html", "booking_reference")
=======
@app.route("/K2", methods=["POST"])
def k2():
    guests = request.form.get("Capacity")
    error = "För stort sällskap"
    query = f"SELECT * FROM K2 ORDER BY pricepernight"
    value = (guests)
    result = execute_query(query,value,fetch_result=True)
    
    if result:
        return render_template("k1.html", result=result)
    else:
        return render_template("error.html",error=error)    
>>>>>>> K2

if __name__ == "__main__":
    app.run(debug=True)

