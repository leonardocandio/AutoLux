import typing
from flask import Flask
from database import db, migrate
from app.oauth import oauth
from app.cache import cache

from app.blueprints.news.models.article import Article
from app.blueprints.shop.models.car import Car
from app.blueprints.shop.models.brand import Brand
from app.blueprints.auth.models.user import User

from app.blueprints.auth.auth_routes import auth
from app.blueprints.home.home_routes import home
from app.blueprints.news.news_routes import news
from app.blueprints.shop.shop_routes import shop
from app.blueprints.forum.forum_routes import forum

from app.utils.web_scraping_cars import create_all_cars
from app.utils.web_scraping_news import create_all_articles
from app.utils.web_scraping_cars import create_all_brands
from app.errors.error_handlers import error_handlers



def create_app():
    """
    Creates app instance with specified type (see config.py)
    config_type:
        'config.Test': Testing-optimized config
        'config.Production': Production config
        'config.Development': Development config - Debug True
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')
    error_handlers(app)

    with app.app_context():
        cache.init_app(app)
        oauth.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)


        #Si tabla articles esta vacía, la llenamos con artículos
        if len(Article.query.all()) == 0:
           create_all_articles(db, Article)

        # Si tabla cars esta vacía, la llenamos con carros
        if len(Car.query.all()) == 0:
            create_all_cars(db, Car)

        # Si tabla brands esta vacía, la llenamos con marcas
        if len(Brand.query.all()) == 0:
           create_all_brands(db, Brand)

        #Creamos nuestro primer usuario administrador
        if User.query.filter_by(username="admin").first() is None:
            db.session.add(User(
                username="admin",
                password="password",
                role="admin"
            ))
            db.session.commit()
            db.session.close()

        app.register_blueprint(home)
        app.register_blueprint(news)
        app.register_blueprint(shop)
        app.register_blueprint(auth)
        app.register_blueprint(forum)

    return app
    