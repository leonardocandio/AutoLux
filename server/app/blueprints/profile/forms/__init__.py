from flask_wtf import FlaskForm
from flask import session
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired, Length
from server.app.blueprints.auth.models.user import User

WRONG_USER_ERROR = 'No eres el usuario correcto'


class ChangeUsernameForm(FlaskForm):
    username = StringField("Nombre", validators=[InputRequired(), Length(3, 80)])
    submit = SubmitField("Guardar")

    def validate(self):
        check_validate = super(ChangeUsernameForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False
        # Does our user exist
        user = User.query.filter_by(
            email=session['user_email']
        ).first()
        if user is None:
            self.username.errors.append(
                WRONG_USER_ERROR
            )
            return False
        return True


class ChangePasswordForm(FlaskForm):
    password = StringField("Contraseña", validators=[InputRequired(), Length(6, 64)])
    submit = SubmitField("Guardar")

    def validate(self):
        check_validate = super(ChangePasswordForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False
        # Does our user exist
        user = User.query.filter_by(
            email=session['user_email']
        ).first()
        if user is None:
            self.email.errors.append(
                WRONG_USER_ERROR
            )
            return False
        return True


class ChangeImageForm(FlaskForm):
    image_url = StringField("Imagen", validators=[InputRequired()])
    submit = SubmitField("Guardar")

    def validate(self):
        check_validate = super(ChangeImageForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False
        # Does our user exist
        user = User.query.filter_by(
            email=session['user_email']
        ).first()
        if user is None:
            self.email.errors.append(
                WRONG_USER_ERROR
            )
            return False
        return True
