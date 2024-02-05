from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt       # pip install bcrypt (Detta är ett bibliotek för att lagra hashtaggade lösen. Skapa en tabell för att lagra admin-användarnamn och token)
from psycopg2 import connect, DatabaseError, pool
from dotenv import load_dotenv
import os
import base64
import secrets    #pip install secrets (för att kunna generera en slumpmässig token)

load_dotenv()

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(16)  # hemlig nyckel
bcrypt = Bcrypt(app)


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
            



# K1
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


# Admin registrering
@app.route("/admin/register", methods=["GET"])
def admin_register_page():
    return render_template("admin_register_page.html", error=None)

@app.route("/admin/register", methods=["POST"])
def admin_register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Hasha lösenordet med bcrypt innan du lagrar det i databasen
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Generera en token för den nya adminen
        token = generate_random_token()

        # Sätt in admin i databasen
        insert_query = "INSERT INTO admins (username, password_hash, token) VALUES (%s, %s, %s) RETURNING id"
        admin_id = execute_query(insert_query, (username, password_hash, token), fetch_result=True)

        # Sätt inloggnings-sessionen för den nya adminen
        session['admin_token'] = token

        return redirect(url_for('admin_dashboard'))

    return render_template('admin_register_page.html', error=None)



# Admin login
@app.route("/admin/login", methods=["GET"])
def admin_login_page():  
    return render_template("admin_login_page.html", error=None)


@app.route("/admin/login", methods=["POST"])
def admin_login():
        username = request.form.get("username")
        password = request.form.get("password")

        # Fråga databasen för att hämta admin med det angivna användarnamnet
        query = "SELECT * FROM hotel.admins WHERE username = %s"
        result = execute_query(query, (username,), fetch_result=True)

        if result and bcrypt.check_password_hash(result[2], password):
            # Om lösenordet är korrekt, generera en token och lagra den i databasen
            token = generate_random_token()
            update_token_query = "UPDATE admins SET token = %s WHERE id = %s"
            execute_query(update_token_query, (token, result[0]))

            # Sätt inloggnings-sessionen för den nya adminen
            session['admin_token'] = token

            # Sätt authenticated till True
            authenticated = True
            if authenticated:
             return redirect(url_for('admin_dashboard'))
            else:
                return render_template('admin_login_page.html', error="Ogiltiga inloggningsuppgifter")
        return render_template('admin_login_page.html', error=None)
    

# implementering av funktionen generate_random_token() enligt ovan
def generate_random_token():
    return secrets.token_urlsafe()  # hemlig nyckel


# efter lyckad inloggning, där admin kan utföra administrativa uppgifter.
@app.route("/admin/dashboard")
def admin_dashboard():
    if 'admin_token' in session:
        return render_template('admin_dashboard.html')
    else:
        return redirect(url_for('admin_login_page'))

    

@app.route("/admin/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        session.pop('admin_token', None)
        return redirect(url_for('admin_logout_page'))
    return redirect(url_for('admin_logout_page'))


@app.route("/admin/logout_page")
def admin_logout_page():
    return render_template('admin_logout_page.html')


if __name__ == "__main__":
    app.run(debug=True)
