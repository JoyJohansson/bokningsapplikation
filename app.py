from flask import Flask, render_template, request, redirect, url_for
from psycopg2 import connect, DatabaseError, pool
from dotenv import load_dotenv
import os
import base64

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

@app.route("/error", methods=["GET", "POST"])
def get_room():
    query = """
    SELECT room_id, roomtype, filename, filetype, file_content, capacity, pricepernight
    FROM room_details
    """
    results = execute_query(query, fetch_result=True)
    
    if results:
        converted_results = []
        for result in results:
            room_id, roomtype, filename, filetype, file_content, capacity, pricepernight = result
            # Konvertera BYTEA-data till Base64-kodad sträng
            file_content_base64 = base64.b64encode(file_content).decode('utf-8')
            # Lägg till konverterad data till resultatlistan
            converted_result = {
                'room_id': room_id,
                'roomtype': roomtype,
                'filename': filename,
                'filetype': filetype,
                'file_content_base64': file_content_base64,
                'capacity': capacity,
                'pricepernight': pricepernight
            }
            converted_results.append(converted_result)
        return render_template("error.html", results=converted_results)
    else:
        return render_template("error.html", error="No data found")

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
    
    

 # Uppdaterat: error meddelandet

        
if __name__ == "__main__":
    app.run(debug=True)

