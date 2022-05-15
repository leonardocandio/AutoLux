from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired, Length, Email
from database import db
from app.blueprints.auth.models.user import User


class LoginForm(FlaskForm):
    email = StringField("Correo", validators=[InputRequired(), Email()])
    password = StringField("Contraseña", validators=[InputRequired()])
    submit = SubmitField("Ingresar")

    def validate(self):
        check_validate = super(LoginForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False
        # Does our user exist
        user = User.query.filter_by(
            username=self.username.data
        ).first()
        if user is None:
            self.email.errors.append(
                'Invalid email or password'
            )
            return False
        # Do the passwords match
        if not user.verify_password(self.password.data):
            self.email.errors.append(
                'Invalid email or password'
            )
            return False
        return True


class RegisterForm(FlaskForm):
    username = StringField("Usuario", validators=[InputRequired()])
    email = StringField("Correo", validators=[InputRequired(), Email()])
    password = StringField("Contraseña", validators=[InputRequired(), Length(6, 64)])
    submit = SubmitField("Registrarse")

    def validate(self):
        check_validate = super(RegisterForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False
        # Does our user exist
        user = User.query.filter_by(
            email=self.email.data
        ).first()
        if user is not None:
            self.email.errors.append(
                'Usuario ya registrado'
            )
            return False
        return True
