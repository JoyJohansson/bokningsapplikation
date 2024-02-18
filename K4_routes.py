from flask import request, render_template, Blueprint
from datetime import datetime
import app

bp = Blueprint('K4_routes', __name__)

@bp.route('/K4_routes')
def K4_routes():
    # Exempel på vad som kan göras i denna ruttfunktion
    return "This is the route function for K4_routes."



# Bokningsbekräftelse
#TODO engelska?
@bp.route('/bekraftelse')
def bekraftelse():
    booking_reference = request.args.get('booking_ref')
    return render_template('bokningsbekräftelse.html', booking_ref=booking_reference)

