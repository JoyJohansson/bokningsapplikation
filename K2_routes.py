from flask import request, render_template, session, Blueprint
import app
import databas
import base64

bp = Blueprint('K2_routes', __name__)

@bp.route("/available_rooms", methods=["POST"])
def k2():
    session["start_date"] = request.form["start_date"]
    session["end_date"] = request.form["end_date"]
    session["selected_guests"] = request.form["guests"]
    check_in_date = request.form.get("start_date")
    check_out_date = request.form.get("end_date")
    guests = request.form.get("guests")
    query = """
    SELECT DISTINCT r.Room_ID, rt.roomtype, f.Filename, f.filetype, f.file_content, rt.capacity, r.pricepernight
    FROM Room r
    LEFT JOIN Booking b ON r.Room_ID = b.room_id
    LEFT JOIN RoomType rt ON r.RoomType_ID = rt.RoomType_ID
    LEFT JOIN Files f ON r.Room_id = f.room_ID
    WHERE (b.room_id IS NULL OR NOT (b.Check_out_date >= %s AND b.Check_in_date <= %s))
    AND rt.capacity >= %s
    """
    print(guests)
    results = databas.execute_query_fetchall(query,(check_in_date,check_out_date,guests,), fetch_result=True)
    
    if results:
        converted_results = []
        for result in results:
            room_id, roomtype,filename, filetype, file_content, capacity, pricepernight = result
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
        return render_template("k1_start.html", error="No data found")

