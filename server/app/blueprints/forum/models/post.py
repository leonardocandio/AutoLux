from server.app.blueprints.auth.models.user import User
from server.app.models.super_models.time_model import TimeModel
from server.database import db

class Post(db.Model, TimeModel):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship(
        'Comment', backref='post', lazy="dynamic"
    )
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post {self.title}>"

    def format(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'body' : self.body,
            'author_id' : self.author_id,
            'last_updated' : self.last_updated
        }


    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()
        user_count = User.query.count()
        for _ in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(title=forgery_py.lorem_ipsum.title(randint(1, 3)),
                     body=forgery_py.lorem_ipsum.sentences(randint(3, 4)),
                     created_at=forgery_py.date.date(True),
                     author=u)
            db.session.add(p)
            db.session.commit()
