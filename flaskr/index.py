from app import app
from models.user import User
from models.article import Article
from models.car import Car
from utils.db import db
from utils.carsapi import create_all_cars
from utils.scraping import create_all_articles

with app.app_context():
    db.create_all()

    # Si tabla articles esta vacia, la llenamos con articulos
    if len(Article.query.all()) == 0:
        create_all_articles(db, Article)

    # Si tabla cars esta vacia, la llenamos con carros
    if len(Car.query.all()) == 0:
        create_all_cars(db, Car)

    # Creamos nuestro primer usuario administrador
    if User.query.filter_by(username="admin").first() is None:
        db.session.add(User(
            username = "admin",
            password = "password",
            role = "admin"
        ))
        db.session.commit()

if __name__ == '__main__':
    app.run()