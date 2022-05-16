from functools import wraps

from flask import (
    redirect, session, url_for, render_template, request,
    abort
)
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.urls import url_parse

from app.blueprints.auth.controller import auth
from app.cache import cache
from app.oauth import oauth
from database import db
from .forms import LoginForm, RegisterForm
from .models.user import User
from .models.role import Permission


@cache.cached(timeout=50)
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username=username, email=email, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            # añádimos la información del usuario a la session
            session['user_username'] = new_user.username
            session['user_email'] = new_user.email
            session['user_image_url'] = new_user.image_url
            session['user_id'] = new_user.id
        except Exception as e:
            print(e)

        login_user(new_user, remember=True)
        return redirect(url_for("home.home_page"))
    return render_template("register.html", form=form)


@cache.cached(timeout=50)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one()
        # añádimos la información del usuario a la session
        session['user_username'] = user.username
        session['user_email'] = user.email
        session['user_image_url'] = user.image_url
        session['user_id'] = user.id
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("home.home_page")
        return redirect(next_page)

    return render_template("login.html", form=form)


@auth.route('/account-recovery')
def recovery():
    return render_template("recovery.html")


@auth.route('/logout')
@login_required
def logout():
    user = current_user
    session['user_username'] = ''
    session['user_email'] = ''
    session['user_image_url'] = ''
    session['user_id'] = ''
    logout_user()
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
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    print(user)
    google_user = User.query.filter_by(email=user.email).first()
    if google_user is None and user is not None:
        new_user = User(username=user.email.split("@")[0], email=user.email, password=user.sub, image_url=user.picture)
        db.session.add(new_user)
        db.session.commit()
        session['user_username'] = new_user.email
        session['user_email'] = new_user.email
        session['user_image_url'] = new_user.image_url
        session['user_id'] = new_user.id
        login_user(new_user)
    elif google_user is not None:
        session['user_username'] = google_user.email
        session['user_email'] = google_user.email
        session['user_image_url'] = google_user.image_url
        session['user_id'] = google_user.id
        login_user(google_user, remember=True)

    return redirect(url_for("home.home_page"))


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
                return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


@auth.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
