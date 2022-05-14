from database import db
from app.models.super_models.time_model import TimeModel


class Comment(db.Model, TimeModel):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f"<Comment {self.id}>"
