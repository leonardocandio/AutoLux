from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.super_models.time_model import TimeModel
from database import db
from .role import Permission


class User(UserMixin, db.Model, TimeModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    nickname = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String,
                          default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=2)
    posts = db.relationship(
        'Post', backref='user', lazy='dynamic'
    )

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_admin(self):
        return self.can(Permission.ADMINISTER)

    @property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.id}>'

    @staticmethod
    def first_user():
        if User.query.filter_by(username="admin").first() is None:
            db.session.add(User(
                username="admin",
                nickname="admin",
                password="password",
                role_id="1"
            ))
            db.session.commit()
            db.session.close()


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_admin(self):
        return False
