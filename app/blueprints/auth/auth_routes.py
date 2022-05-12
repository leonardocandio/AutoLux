from functools import wraps
import re
from app.blueprints.auth import auth
from database import db
from .models.user import User
from app.cache import cache
from app.oauth import oauth
from flask import (
    redirect, url_for, render_template, request,
    session, g, flash, session, jsonify
)

@cache.cached(timeout=50)
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        message = ''

        # Ver si existe alguien con el mismo usuario
        if username == "" or password == "":
            flash('Username and password are required', 'danger')
            return render_template("register.html")

        if len(username) < 5 or len(password) < 5:
            flash('Username and password must be at least 5 characters', 'danger')
            return render_template("register.html")

        if User.query.filter_by(username=username).first() is not None:
            flash('Someone else with that username already exists', 'danger')
            return render_template("register.html")

        # Se crea el usuario
        new_user = User(username=username, password=password, role='user')
        db.session.add(new_user)
        db.session.commit()
        session.clear()
        session['user_id'] = new_user.id

        return redirect("/")
    return render_template("register.html")

@cache.cached(timeout=50)
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if username == "" or password == "":
            flash('Username field or password field are empty', 'danger')
            return render_template("login.html")

        if user is None:
            flash('User not found', 'danger')
            return render_template("login.html")

        if password != user.password:
            flash('Your password are incorrect', 'danger')
            return render_template("login.html")

        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('home.home_page'))

    google = oauth.create_client('google')
    redirect_uri = 'http://localhost:5000/authorize'
    
    return render_template("login.html")

@auth.route('/account-recovery')
def recovery():
    return render_template("recovery.html")

@auth.route('/logout')
def logout():
    if session.get('profile') is not None:
        session['profile'] = None
    else:
        session['user_id'] = None
    return redirect('/login')

@auth.route('/login_google')
def login_google():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['user'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    print(user)
    return redirect('/')



@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None and session.get('user') is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None and session.get('user') is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view


def admin_role_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user.role != "admin":
            flash("Admin role is required", 'danger')
            return redirect(url_for('auth.login', next=request.url))

        return view(**kwargs)

    return wrapped_view


