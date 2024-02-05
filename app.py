from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt       # pip install bcrypt (Detta är ett bibliotek för att lagra hashtaggade lösen. Skapa en tabell för att lagra admin-användarnamn och token)
from psycopg2 import connect, DatabaseError, pool
from dotenv import load_dotenv
from datetime import datetime

import os
import secrets    #pip install secrets (för att kunna generera en slumpmässig token)
import re  # re.match för att jämföra e-postadresserna med ett reguljärt uttryck.
import time
import random


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
                return cursor.fetch()
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

@app.route("/error")
def error():
    return "Something went wrong"





# email
@app.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        epost1 = request.form['epost1']
        epost2 = request.form['epost2']
        booking_reference = generate_booking_reference()  # Replace this with your logic to generate a reference
        return redirect(url_for('bekraftelse', booking_ref=booking_reference))
    return render_template('e-post.html')


# Bokningsbekräftelse
@app.route('/bekraftelse')
def bekraftelse():
    booking_reference = request.args.get('booking_ref')
    return f"Bokningsbekräftelse: Tack för din bokning! Bokningsreferens: {booking_reference}"

# Bokningsreferens
def generate_booking_reference():
    # realtid timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # generera slumpmässig sträng på 6 tecken
    random_string = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    # kombinera timestamp med sträng för att skapa unique bokningsreferens
    booking_reference = f'{timestamp}{random_string}'
    return booking_reference







# Query for databas
create_table_query = """
CREATE TABLE IF NOT EXISTS admins (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    token VARCHAR(256)
);
"""
execute_query(create_table_query, (), fetch_result=False)


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
    if request.method == "POST":
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