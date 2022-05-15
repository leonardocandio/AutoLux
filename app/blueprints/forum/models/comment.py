from database import db
from app.models.super_models.time_model import TimeModel


class Comment(db.Model, TimeModel):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    body = db.Column(db.Text)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f"<Comment {self.id}>"
