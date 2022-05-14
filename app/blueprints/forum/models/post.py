from app.models.super_models.time_model import TimeModel
from database import db


class Post(db.Model, TimeModel):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text())
    author = db.Column(db.Integer(), db.ForeignKey('users.id'))
    comments = db.relationship(
        'Comment', backref='posts', lazy="dynamic"
    )

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def __repr__(self):
        return f"<Post {self.title}>"
