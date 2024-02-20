from flask import render_template, redirect, url_for, jsonify, Blueprint
import app
import databas
import datetime
import utils
from datetime import datetime


bp = Blueprint('contact_routes', __name__)

@bp.route("/contacts", methods=["GET"])
def get_hotell():
    query = """
    SELECT Name, Country, City, Address, Email, Phone
    FROM Hotel
    """
    results = databas.execute_query_fetchall(query, fetch_result=True)
    
    if results:
        return render_template("contacts.html", results=results)
    else:
        return render_template("contacts.html", error="No data found")
      