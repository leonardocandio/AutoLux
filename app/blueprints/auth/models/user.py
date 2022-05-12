from app.models.super_models.time_model import TimeModel
from database import db


class User(db.Model, TimeModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture"
                                             "-973460__340.png")
    role = db.Column(db.String(20), nullable=False)
    posts = db.relationship(
        'Post', backref='user', lazy='dynamic'
    )

    def __repr__(self):
        return f'<User {self.id}>'

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
