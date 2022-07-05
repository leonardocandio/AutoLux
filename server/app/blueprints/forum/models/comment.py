from server.app.models.super_models.time_model import TimeModel
from server.database import db


class Comment(db.Model, TimeModel):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    body = db.Column(db.Text)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def format(self):
        return {
            'id': self.id,
            'body': self.body,
            'author': self.author.format(),
            'last_updated': self.last_updated,
            'post_id': self.post_id,
            'created_at': self.created_at,
            'disabled': self.disabled
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Comment {self.id}>"
