from flask import Flask, render_template, request, redirect, url_for, session, jsonify
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
    return render_template("k1_start.html")

def generate_random_code():
    return random.randint(100000, 999999)

@app.route("/contacts", methods=["GET", "POST"])
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
        return render_template("contacts.html", results=converted_results)
    else:
        return render_template("contacts.html", error="No data found")
      
@app.route("/available_rooms", methods=["POST"])
def k2():
    session["start_date"] = request.form["start_date"]
    session["end_date"] = request.form["end_date"]
    session["selected_guests"] = request.form["guests"]
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
        return render_template("k2_available_rooms.html", results=converted_results)
    else:
        return render_template("contacts.html", error="No data found")

# email
@app.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        epost1 = request.form['epost1']
        epost2 = request.form['epost2']
        booking_reference = generate_booking_reference()
        return redirect(url_for('bekraftelse', booking_ref=booking_reference))
    return render_template('k4_booking_details.html')


# Bokningsbekräftelse
#TODO engelska?
@app.route('/bekraftelse')
def bekraftelse():
    booking_reference = request.args.get('booking_ref')
    return f"Bokningsbekräftelse: Your booking is confirmed. Your bookningsreference is: {booking_reference}"

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
@app.route("/admin/register", methods=["GET"])
def admin_register_page():
    return render_template("admin_register_page.html", error=None)

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
@app.route("/admin/login", methods=["GET"])
def admin_login_page():  
    return render_template("admin_login_page.html", error=None)
  
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
    return render_template("k3_room_info.html", room=room)


@app.route("/book", methods=["POST"])
def book_room():
    args = request.form
    room_id = args["room_id"]
    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)
    return render_template("k4_booking_details.html", room=room)

@app.route("/save_booking", methods=["POST"])
def save_booking():
    print("save_booking")
    print(session)
    room_id = request.form.get("room_id")
    email = request.form.get("email")
    name = request.form.get("name")
    start_date = session.get("start_date")
    end_date = session.get("end_date")
    selected_guests = session.get("selected_guests")
    bookingID = generate_booking_reference()
    #TODO guest_id som en autoincrementerad serial
    #TODO fixa queryn
    create_guest_query = """INSERT INTO guest_details (name, email)
                        VALUES (%s, %s)"""
    guest_saved = databas.execute_insert_query(create_guest_query, (name,email))
    print(guest_saved)
    #TODO lägg till room_id i db booking
    #TODO få denna query att funka
    query = "SELECT Guest_ID FROM guest_details WHERE name = %s"
    result = databas.execute_query_fetchone(query,(name,),fetch_result=True)
    #TODO status som en warchar
    insert_query = """INSERT INTO booking (booking_id, guest_id,room_id, check_in_date, check_out_date, status)
                    VALUES (%s,%s, %s,%s,%s, True)"""
    databas.execute_insert_query(insert_query, (bookingID,result,room_id,start_date, end_date,))
    #TODO göra en view så vi får upp booking från Databasen
    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)
    return render_template("k4_booking_details.html", room=room, start_date=start_date,end_date=end_date, selected_guests=selected_guests,name=name,email=email)


# Hämta bokning via bokningsreferens och omdirigera till kundens kontrollpanel
@app.route("/get_booking/<booking_reference>", methods=["GET"])
def get_booking(booking_reference):
    query = "SELECT * FROM booking WHERE booking_id = %s"
    result = databas.execute_query_fetchone(query, (booking_reference), fetch_result=True)
    if result:
        # omdirigera till kundens kontrollpanel
        return render_template('K8_guest_dashboard).html')
    else:
        return {"error": "Booking not found"}, 404



# Avboka
def mark_booking_as_cancelled(booking_reference):
    # Uppdatera databasen för att markera bokningen som avbokad med en timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_query = "UPDATE booking SET cancelled_at = %s WHERE booking_reference = %s"
    databas.execute_insert_query(update_query, (timestamp, booking_reference))

# Avbokningsbekräftelse
@app.route('/booking_cancelled')
def booking_cancelled():
    return render_template('booking_cancelled.html')


# gäst_kontrollpanell
@app.route('/guest_control_panel')
def guest_control_panel():
    # Hämta bokningsinformation baserat på användarens session
    booking_reference = session.get("booking_reference")
    query = "SELECT * FROM booking WHERE booking_ID = %s"
    booking_info = databas.execute_query_fetchone(query, (booking_reference,), fetch_result=True)

    if booking_info:
        # Extrahera relevant information från bokningsdata
        room_id = booking_info[2]
        email = booking_info[3]
        name = booking_info[4]
        start_date = booking_info[5]
        end_date = booking_info[6]
        selected_guests = booking_info[7]

        return render_template('K8_guest_dashboard.html', room_id=room_id, name=name, email=email, start_date=start_date, end_date=end_date, selected_guests=selected_guests)
    else:
        return render_template('K8_guest_dashboard.html', error="Bokning inte hittad")


# Logga ut
@app.route('/logout', methods=['POST'])
def guest_logout_page():
    # Koden för utloggning, till exempel att rensa sessionen
    return render_template('guest_logout_page.html')


if __name__ == "__main__":
    app.run(debug=True)
