from functools import wraps

from flask import abort, jsonify, request
from flask_login import login_user, login_required, logout_user, current_user

from server.app.blueprints.users.controller import users
from server.app.blueprints.users.models.role import Permission
from server.app.blueprints.users.models.user import User
from server.app.cache import cache


@cache.cached(timeout=50)
@users.route('/', methods=['POST'])
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
            'message': 'User created successfully',
            'user': new_user.format()
        })
    abort(400)


@users.route('/session', methods=['GET'])
def logged_in():
    return jsonify({
        'code': 200,
        'success': True,
        'message': 'User is logged in',
        'user': current_user.format()
    })


@users.route('/session', methods=['DELETE'])
def logout():
    logout_user()
    return jsonify({
        'code': 200,
        'success': True,
        'message': 'User logged out successfully'
    })


@cache.cached(timeout=50)
@users.route('/session', methods=['POST'])
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


@users.route('/<id>', methods=['GET'])
def get_profile_page(id):
    user = User.query.get_or_404(id)
    return jsonify({
        'code': 200,
        'success': True,
        'message': 'User found',
        'permissions': True,
        'user': user.format()
    })

