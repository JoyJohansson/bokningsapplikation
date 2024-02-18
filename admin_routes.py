from flask import request, render_template, session, redirect, url_for, Blueprint
import databas
from authentication import generate_secret_key, generate_random_token
import bcrypt
from flask_bcrypt import generate_password_hash, check_password_hash



bp = Blueprint('admin_routes', __name__)
bp.secret_key = 'your_secret_key'


# Admin registrering
@bp.route("/admin/register", methods=["GET"])
def admin_register_page():
    return render_template("admin_register_page.html", error=None)

# Admin registrering
@bp.route("/admin/register", methods=["POST"])
def admin_register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Hasha lösenordet med bcrypt innan du lagrar det i databasen
        password_hash = generate_password_hash(password).decode('utf-8')


        # Generera en token för den nya adminen
        token = generate_random_token()

        # Sätt in admin i databasen
        insert_query = "INSERT INTO admins (username, password_hash, token) VALUES (%s, %s, %s) RETURNING id"
        databas.admin_id = databas.execute_query_fetchall(insert_query, (username, password_hash, token), fetch_result=True)

        # Sätt inloggnings-sessionen för den nya adminen
        session['admin_token'] = token

        return redirect(url_for('admin_routes.admin_dashboard'))

    return render_template('admin_register_page.html', error=None)

# Admin login
@bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login_page():
    if request.method == 'POST':
        return redirect(url_for('admin_routes.admin_dashboard'))
    return render_template('admin_login_page.html')

# Admin login
@bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        query = "SELECT * FROM admins WHERE username = %s"
        result = databas.execute_query_fetchall(query, (username, password), fetch_result=True)

        if result and bcrypt.check_password_hash(result[2], password):
            token = generate_random_token()
            update_token_query = "UPDATE admins SET token = %s WHERE id = %s"
            databas.execute_insert_query(update_token_query, (token, result[0]))

            session['admin_token'] = token

            return redirect(url_for('admin_routes.admin_dashboard'))
        else:
            return render_template('admin_login_page.html', error="Ogiltiga inloggningsuppgifter")

    return render_template('admin_login_page.html')


# efter lyckad inloggning, där admin kan utföra administrativa uppgifter.
@bp.route("/admin/dashboard")
def admin_dashboard():
    if 'admin_token' in session:
        return render_template('admin_dashboard.html', admin_token=session.get('admin_token'))
    else:
        return redirect(url_for('admin_routes.admin_login'))

    
      

@bp.route("/admin/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        session.pop('admin_token', None)
        return redirect(url_for('admin_routes.admin_logout_page'))
    

@bp.route("/admin/logout_page")
def admin_logout_page():
    return render_template('admin_logout_page.html')
