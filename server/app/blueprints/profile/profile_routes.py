from flask import render_template, redirect, url_for, abort, session, jsonify, request
from flask_login import current_user, login_required
from server.database import db
from server.app.blueprints.profile.controller import profile
from server.app.blueprints.auth.models.user import User
from ..auth.models.role import Permission
from .forms import ChangeUsernameForm, ChangePasswordForm, ChangeImageForm

@profile.route('/<id>', methods=['GET'])
def get_profile_page(id):
    user = User.query.get_or_404(id)
    permissions = current_user.id == user.id
    return jsonify({
        'code': 200,
        'success': True,
        'message': 'User found',
        'permissions': permissions,
        'user': user.format()
    })





@profile.route('/<id>', methods=['PATCH'])
def profile_page(id):
    user = User.query.get_or_404(id)
    res = request.get_json()

    pass


@profile.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@profile.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
