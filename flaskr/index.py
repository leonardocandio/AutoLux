from app import app
from models.user import User
from utils.db import db

with app.app_context():
    db.create_all()
    if User.query.filter_by(username="admin").first() is None:
        db.session.add(User(
            username = "admin",
            password = "password",
            role = "admin"
        ))
        db.session.commit()


if __name__ == '__main__':
    app.run()