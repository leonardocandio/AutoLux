from functools import wraps

from flask import (
    redirect, session, url_for, render_template, request,
    abort, jsonify
)
from flask_login import login_user, login_required, logout_user, current_user

from server.app.blueprints.auth.controller import auth
from server.app.cache import cache
from server.app.oauth import oauth
from server.database import db
from .models.role import Permission
from .models.user import User


@cache.cached(timeout=50)
@auth.route('/register', methods=['POST'])
def register():
    body = request.get_json()
    username = body.get('username', None)
    email = body.get('email', None)
    password = body.get('password', None)

    if User.validate_register(email):
        new_user = User(username=username, email=email, password=password)
        try:
            new_user.insert()
        except Exception:
            abort(500)
        login_user(new_user, remember=True)
        return jsonify({
            'code': 200,
            'success': True,
            'message': 'User created successfully'
        })
    abort(400)


@cache.cached(timeout=50)
@auth.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({
            'code': 200,
            'success': True,
            'message': 'User already logged in',
            'user': current_user.format()
        })

    body = request.get_json()
    email = body.get('email', None)
    password = body.get('password', None)

    user = User.validate_login(email, password)

    if user:
        login_user(user, remember=True)
        return jsonify({
            'code': 200,
            'success': True,
            'message': 'User logged in successfully',
            'user': user.format()
        })

    abort(401)


@auth.route('/account-recovery')
def recovery():
    return render_template("recovery.html")


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({
        'code': 200,
        'success': True,
        'message': 'User logged out successfully'
    })


@auth.route('/google-login')
def login_google():
    google = oauth.create_client('google')  # insert the google oauth client
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # insert the google oauth client
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


# --------------- POST GET -----------------#

# --------------- CARS GET -----------------#





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
