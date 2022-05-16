from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = TextAreaField(validators=[InputRequired()])
    body = TextAreaField("¿En que estas pensando?", validators=[InputRequired()])
    submit = SubmitField('Publicar')


class CommentForm(FlaskForm):
    body = TextAreaField("Comenta", validators=[InputRequired()])
