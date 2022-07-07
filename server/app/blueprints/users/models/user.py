from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from server.app.models.super_models.time_model import TimeModel
from server.database import db
from .role import Permission


class User(UserMixin, db.Model, TimeModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String,
                          default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=2)
    posts = db.relationship(
        'Post', backref='author', lazy='dynamic'
    )
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'image_url': self.image_url,
            'role_id': self.role_id,
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'posts': [post.format_short() for post in self.posts.all()]
        }

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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.id}>'

    @staticmethod
    def validate_login(_email, password):
        print(_email)
        user = User.query.filter_by(email=_email).one_or_none()
        if user is None:
            return False
        if not user.verify_password(password):
            return False
        return user

    @staticmethod
    def validate_register(_email):
        user = User.query.filter_by(email=_email).one_or_none()
        if user is not None:
            return False
        return True

    @staticmethod
    def first_user():
        if User.query.filter_by(username="admin").first() is None:
            db.session.add(User(
                username="admin",
                email="admin@gmail.com",
                password="password",
                role_id="1"
            ))
            db.session.commit()
            db.session.close()

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for _ in range(count):
            n = forgery_py.internet.user_name(True)
            u = User(username=n, email=forgery_py.internet.email_address(),
                     password=forgery_py.lorem_ipsum.word())

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_admin(self):
        return False
