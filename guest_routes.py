from flask import request, render_template, session, redirect, url_for, Blueprint
import app
import databas

bp = Blueprint('guest_routes', __name__)



@bp.route("/guest/login", methods=["GET", "POST"])
def guest_login():
    if request.method == "POST":
        booking = request.form["booking_id"]
        
        # Kontrollera om gästen existerar i databasen baserat på e-postadressen
        query = "SELECT * FROM booking WHERE booking_id = %s"
        result = databas.execute_query_fetchone(query, (booking,), fetch_result=True)
        
        if result:
            booking_id = result[0]
            # Spara gästens ID i sessionen
            session["booking_id"] = booking_id
            # Omdirigera till dashboard-sidan efter inloggning
            return redirect(url_for("guest_booking"))
        
        # Om inloggningen misslyckas, visa ett felmeddelande
        return render_template("guest_login.html", error="Ogiltig bokingsreferens")
    
    return render_template("guest_login.html", error=None)


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
        return redirect(url_for("guest_login"))

def final_price(start, end, price):
    amount_of_days = (end - start)
    total_price = (amount_of_days * price)
    return total_price

@bp.route("/guest/logout", methods=["POST"])
def guest_logout():
    if request.method == "POST":
        session.pop("booking_id", None)
        return redirect(url_for('guest_logout_page'))
    else:
        return "Method Not Allowed", 405


@bp.route("/guest/logout_page")
def guest_logout_page():
    return render_template('guest_logout_page.html')