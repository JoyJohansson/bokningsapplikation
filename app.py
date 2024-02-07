from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt 
from psycopg2 import connect, DatabaseError, pool
from dotenv import load_dotenv
from datetime import datetime
import os
import base64
import secrets 
import random
import databas


load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
bcrypt = Bcrypt(app)

# K1
@app.route("/")
def k1():
    return render_template("k1.html")

#TODO ändra route
@app.route("/error", methods=["GET", "POST"])
def get_room():
    query = """
    SELECT room_id, roomtype, filename, filetype, file_content, capacity, pricepernight
    FROM room_details
    """
    results = databas.execute_query_fetchall(query, fetch_result=True)
    
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
      
#TODO mer beskrivande route?
@app.route("/K2", methods=["POST"])
def k2():
    query = """
    SELECT room_id, roomtype, filename, filetype, file_content, capacity, pricepernight
    FROM room_details
    """
    results = databas.execute_query_fetchall(query, fetch_result=True)
    
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
        return render_template("k2.html", results=converted_results)
    else:
        return render_template("error.html", error="No data found")
      
###@app.route("/K2", methods=["POST"])
def k2w():
    guests = request.form.get("guests")
    error = "För stort sällskap"
    query = "SELECT Roomtype,Room_ID FROM K2 WHERE Capacity >= %s ORDER BY PricePerNight"
    value = (guests)
    result = databas.execute_query_fetchall(query,value,fetch_result=True)
    
    if result:
        return render_template("k1.html", result=result)
    else:
        return render_template("error.html",error=error) 

# email
@app.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        epost1 = request.form['epost1']
        epost2 = request.form['epost2']
        booking_reference = generate_booking_reference()
        return redirect(url_for('bekraftelse', booking_ref=booking_reference))
    return render_template('e-post.html')


# Bokningsbekräftelse
#TODO engelska?
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

# Admin registrering
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
        admin_id = databas.execute_query_fetchone(insert_query, (username, password_hash, token), fetch_result=True)

        # Sätt inloggnings-sessionen för den nya adminen
        session['admin_token'] = token

        return redirect(url_for('admin_dashboard'))

    return render_template('admin_register_page.html', error=None)

  
# Admin login
@app.route("/admin/login", methods=["POST"])
def admin_login():
        username = request.form.get("username")
        password = request.form.get("password")

        # Fråga databasen för att hämta admin med det angivna användarnamnet
        query = "SELECT * FROM admins WHERE username = %s"
        result = databas.execute_query_fetchone(query, (username,), fetch_result=True)
        print(result)

        if result and bcrypt.check_password_hash(result[2], password):
            # Om lösenordet är korrekt, generera en token och lagra den i databasen
            token = generate_random_token()
            update_token_query = "UPDATE admins SET token = %s WHERE id = %s"
            databas.execute_insert_query(update_token_query, (token, result[0]))

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

@app.route("/room_info", methods=["GET"])
def room_info():
    args = request.args
    room_id = args["room_id"]
    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)
    print (room)
    print(room_id)
    return render_template("k3.html", room=room)


@app.route("/book", methods=["POST"])
def book_room():
    args = request.form
    room_id = args["room_id"]
    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)
    return render_template("k4.html", room=room)

if __name__ == "__main__":
    app.run(debug=True)
