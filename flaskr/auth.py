from functools import wraps
from utils.db import db
from models.user import User
from flask import (
    Blueprint, redirect, url_for, render_template, request,
    session, g, flash
)

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        message = ''

        # Ver si existe alguien con el mismo usuario
        if username == "" or password == "":
            flash('Username and password are required', 'danger')
            return render_template("auth/register.html")

        if len(username) < 5 or len(password) < 5:
            flash('Username and password must be at least 5 characters', 'danger')
            return render_template("auth/register.html")

        if User.query.filter_by(username=username).first() is not None:
            flash('Someone else with that username already exists', 'danger')
            return render_template("auth/register.html")

        # Se crea el usuario
        new_user = User(username=username, password=password, role='user')
        db.session.add(new_user)
        db.session.commit()
        session.clear()
        session['user_id'] = new_user.id

        return render_template("auth/register.html")
    return render_template("auth/register.html")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if username == "" or password == "":
            flash('Username field or password field are empty', 'danger')
            return render_template("auth/login.html")

        if user == None:
            flash('User not found', 'danger')
            return render_template("auth/login.html")

        if password != user.password:
            flash('Your password are incorrect', 'danger')
            return render_template("auth/login.html")

        session.clear()
        session['user_id'] = user.id
        return redirect('/')

    return render_template("auth/login.html")


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id == None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
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
