from flask import request, render_template, session, Blueprint
from datetime import datetime
import app
import databas

bp = Blueprint('K3_routes', __name__)

@bp.route("/room_info", methods=["GET"])
def room_info():
    args = request.args
    room_id = args["room_id"]
    query = "SELECT Room_ID, Roomtype, PricePerNight FROM room, RoomType WHERE room_id = %s"
    room = databas.execute_query_fetchone(query, (room_id,), fetch_result=True)

    start_date = datetime.strptime(session.get("start_date"), "%Y-%m-%d")
    end_date = datetime.strptime(session.get("end_date"), "%Y-%m-%d")

    num_days = (end_date - start_date).days


    total_price = num_days * float(room[2])
    print (room)
    print(room_id)
    return render_template("k3_room_info.html", room=room, total_price=total_price)
