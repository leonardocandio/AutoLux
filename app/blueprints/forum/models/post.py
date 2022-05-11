from database import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    comments = db.relationship(
        'Comment', backref='posts', lazy="dynamic"
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"<Post {self.title}>"
