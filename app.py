from flask import Flask
from flask_bcrypt import Bcrypt 
import authentication 
import K1_routes
import K2_routes
import K3_routes
import K4_routes
import admin_routes
import guest_routes
import booking_routes


app = Flask(__name__)
app.secret_key = authentication.generate_secret_key()
bcrypt = Bcrypt(app)

app.register_blueprint(K1_routes.bp)
app.register_blueprint(K2_routes.bp)
app.register_blueprint(K3_routes.bp)
app.register_blueprint(K4_routes.bp)
app.register_blueprint(admin_routes.bp)
app.register_blueprint(guest_routes.bp)
app.register_blueprint(booking_routes.bp)


if __name__ == "__main__":
    app.run(debug=True)
