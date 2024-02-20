from flask import render_template, Blueprint
import app
import utils
import databas
import random

bp = Blueprint('K1_routes', __name__)

@bp.route("/")
def k1():
    return render_template("k1_start.html")


