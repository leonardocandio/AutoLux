from app import app
from models.user import User
from models.article import Article
from utils.db import db
from utils.scraping import create_all_articles

with app.app_context():
    db.create_all()

    # Si tabla articles esta vacia, la llenamos con articulos
    if len(Article.query.all()) == 0:
        create_all_articles(db, Article)

    # Creamos nuestro primer usuario administrador
    if User.query.filter_by(username="admin").first() is None:
        db.session.add(User(
            username = "admin",
            password = "password",
            role = "admin"
        ))
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)