from flask import Flask

from app.blueprints.auth.models.user import User
from app.blueprints.news.models.article import Article
from app.blueprints.shop.models.car import Car
from app.blueprints.forum.models.post import Post
from app.blueprints.forum.models.comment import Comment

from app.blueprints.auth import create_module as auth_create_module
from app.blueprints.forum import create_module as forum_create_module
from app.blueprints.home import create_module as home_create_module
from app.blueprints.news import create_module as news_create_module
from app.blueprints.shop import create_module as shop_create_module

from app.cache import cache
from app.oauth import oauth

from app.utils.web_scraping_cars import create_all_cars
from app.utils.web_scraping_news import create_all_articles

from database import db, migrate


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

    with app.app_context():
        cache.init_app(app)
        oauth.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)

        auth_create_module(app)
        shop_create_module(app)
        news_create_module(app)
        home_create_module(app)
        forum_create_module(app)

    return app
