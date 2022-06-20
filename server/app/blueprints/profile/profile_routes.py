from flask import render_template, redirect, url_for, abort, session
from flask_login import current_user, login_required
from server.database import db
from server.app.blueprints.profile.controller import profile
from server.app.blueprints.auth.models.user import User
from ..auth.models.role import Permission
from .forms import ChangeUsernameForm, ChangePasswordForm, ChangeImageForm


@profile.route('/<id>', methods=['GET', 'POST'])
def profile_page(id):
    user = User.query.filter_by(id=id).first()
    print("current user id: ",current_user.id)
    print("session user: ", session['user_id'])
    form1 = ChangeUsernameForm()
    if form1.validate_on_submit():
        username = form1.username.data
        try:
            u = User.query.filter_by(email=session['user_email']).first()
            u.username = username
            db.session.commit()
            session['user_username'] = username
        except Exception as e:
            print(e)

        return redirect(url_for("profile.profile_page", id=user.id))

    form2 = ChangePasswordForm()
    if form2.validate_on_submit():
        password = form2.password.data
        try:
            u = User.query.filter_by(email=session['user_email']).first()
            u.password = password
            db.session.commit()
            session['user_password'] = password
        except Exception as e:
            print(e)

        return redirect(url_for("profile.profile_page", id=user.id))

    form3 = ChangeImageForm()
    if form3.validate_on_submit():
        image_url = form3.image_url.data
        try:
            u = User.query.filter_by(email=session['user_email']).first()
            u.image_url = image_url
            db.session.commit()
            session['user_image_url'] = image_url
        except Exception as e:
            print(e)

        return redirect(url_for("profile.profile_page", id=user.id))

    if user is None:
        abort(404)

    return render_template('profile.html', user=user, form1=form1, form2=form2, form3=form3)


@profile.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@profile.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
