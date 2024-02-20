from flask import request, render_template, session, redirect, url_for, jsonify, Blueprint
import app
import databas
import datetime
import utils
from datetime import datetime

bp = Blueprint('booking_routes', __name__)


@bp.route("/book", methods=["POST"])
def book_room():
    args = request.form
    room_id = args["room_id"]
    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)
    return render_template("k4_booking_confirmation.html", room=room)

@bp.route("/save_booking", methods=["POST"])
def save_booking():
    print("save_booking")
    print(session)
    
    #VARIABLAR från html k3_room_info.html
    selected_options = request.form.getlist('options')
    booking_ID = request.form.get("booking_ID")
    room_id = request.form.get("room_id")
    email = request.form.get("epost1")
    name = request.form.get("name")
    start_date = session.get("start_date")
    end_date = session.get("end_date")
    selected_guests = session.get("selected_guests")
    booking_ID = utils.generate_booking_reference()
    
    
    start_date = datetime.strptime(session.get("start_date"), "%Y-%m-%d")
    end_date = datetime.strptime(session.get("end_date"), "%Y-%m-%d")
    room_price = float(request.form.get("price_per_night"))


    num_days = (end_date - start_date).days


    utils.total_price = num_days * room_price

    
    #Insert för att lägga till namn och emil i guest_details tabellen
    create_guest_query = """INSERT INTO guest_details (name, email)
                        VALUES (%s, %s)"""
    guest_saved = databas.execute_insert_query(create_guest_query, (name,email))
    print(guest_saved)
    #hämtar gästens ID
    query = "SELECT Guest_ID FROM guest_details WHERE name = %s"
    result = databas.execute_query_fetchone(query,(name,),fetch_result=True)
    #TODO status som en warchar
    #skapar bookningen
    insert_query = """INSERT INTO booking (booking_id, guest_id,room_id, check_in_date, check_out_date, status)
                    VALUES (%s,%s, %s,%s,%s, True)"""
    databas.execute_insert_query(insert_query, (booking_ID,result,room_id,start_date, end_date,))

    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)
    
    print(selected_options)
    
    insert_query = """INSERT INTO bookingoption (booking_id, option_id) VALUES (%s,%s)"""

    for option_value in selected_options:
        
        select_query = "SELECT option_id FROM option WHERE name = %s"
        option_ids = databas.execute_query_fetchall(select_query, (option_value,), fetch_result=True)

        
        if option_ids:
            
            for option_id in option_ids:
                
                databas.execute_insert_query(insert_query, (booking_ID, option_id[0],))
        else:
            #TEST FÖR BACKEND FÖR ATT SE SÅ DEN TAR MED ALLA VARIABLAR
            print(f"Option ID för '{option_value}' hittades inte i databasen.")
    
    return render_template("k4_booking_confirmation.html", booking_ID=booking_ID, room=room, start_date=start_date, end_date=end_date, selected_guests=selected_guests, name=name, email=email)

@bp.route("/guest/booking", methods=["GET"])
def guest_booking():
    # Kontrollera om boknings-id finns i sessionsdata
    if "booking_id" in session:
        booking_id = session["booking_id"]
        
        # SQL-fråga för att hämta bokningsinformation från databasen
        query = """
            SELECT Booking.*, Guest_Details.*, Room.*, RoomType.*
            FROM Booking
            JOIN Guest_Details ON Booking.guest_id = Guest_Details.guest_id
            JOIN Room ON Booking.room_id = Room.Room_ID
            JOIN RoomType ON Room.RoomType_ID = RoomType.RoomType_ID
            WHERE Booking.booking_id = %s AND Booking.status = True
        """
        # Utför SQL-frågan med boknings-id som parameter
        bookings = databas.execute_query_fetchall(query, (booking_id,), fetch_result=True)
        
        # Om ingen bokning hittades, returnera ett meddelande och omdirigera till inloggningssidan
        if not bookings:
            return render_template ("guest_login.html",error="Booking not found")
        
        # Om bokningen hittades, rendera sidan för gästbokningen med bokningsinformationen
        return render_template("guest_booking.html", bookings=bookings)
    else:
        # Om gästen inte är inloggad, omdirigera dem till inloggningssidan
        return redirect(url_for("guest_routes.guest_login"))


    
def final_price(start, end, price):
    amount_of_days = (end - start)
    total_price = (amount_of_days * price)
    return total_price

    
@bp.route("/cancel_booking", methods=["GET"])
def cancel_booking():
    if request.method == "GET":
        booking_id = request.args.get("booking_id")

        
        status_query = "SELECT status FROM booking WHERE booking_id = %s"
        status_result = databas.execute_query_fetchone(status_query, (booking_id,), fetch_result=True)

        if status_result and status_result[0]:
            
            update_query = "UPDATE booking SET status = False WHERE booking_id = %s"
            databas.execute_insert_query(update_query, (booking_id,))

            return jsonify(message="Booking canceled successfully", redirect_url=url_for('guest_routes.guest_logout_page'))
        
        else:
            # If the booking is already canceled, return a message indicating it
            return jsonify(message="This booking has already been canceled", redirect_url=url_for('K1_routes.k1'))



