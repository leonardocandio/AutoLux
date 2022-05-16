from flask import jsonify, render_template, session, request, redirect, url_for, abort

from database import db
from app.blueprints.profile.controller import profile
from app.blueprints.auth.models.user import User
from ..auth.models.role import Permission
from .forms import ChangeUsernameForm, ChangePasswordForm, ChangeImageForm

@profile.route('/<username>', methods=['GET', 'POST'])
def profile_page(username):
    form1 = ChangeUsernameForm()
    if form1.validate_on_submit():
        username = form1.username.data
        try:
            user = User.query.filter_by(email=session['user_email']).first()
            user.username = username
            db.session.commit()
            session['user_username'] = username
        except Exception as e:
            print(e)
        
        return redirect(url_for("profile.profile_page", username=session['user_username']))

    form2 = ChangePasswordForm()
    if form2.validate_on_submit():
        password = form2.username.data
        try:
            user = User.query.filter_by(email=session['user_email']).first()
            user.password = password
            db.session.commit()
            session['user_password'] = password
        except Exception as e:
            print(e)

        return redirect(url_for("profile.profile_page", username=session['user_username']))

    form3 = ChangeImageForm()
    if form3.validate_on_submit():
        image_url = form3.image_url.data
        try:
            user = User.query.filter_by(email=session['user_email']).first()
            user.image_url = image_url
            db.session.commit()
            session['user_image_url'] = image_url
        except Exception as e:
            print(e)

        return redirect(url_for("profile.profile_page", username=session['user_username']))

    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    return render_template('profile.html', user=user, form1=form1, form2=form2, form3=form3)


@profile.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
