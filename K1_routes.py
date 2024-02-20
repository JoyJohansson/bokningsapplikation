from flask import render_template, Blueprint
import app
import utils
import databas
import random
from datetime import datetime

bp = Blueprint('K1_routes', __name__)

@bp.route("/")
def k1():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template("k1_start.html")


