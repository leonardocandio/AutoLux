from flask import Flask
from flask_cors import CORS

from server.app.blueprints.auth import create_module as auth_create_module
from server.app.blueprints.forum import create_module as forum_create_module
from server.app.blueprints.home import create_module as home_create_module
from server.app.blueprints.news import create_module as news_create_module
from server.app.blueprints.profile import create_module as profile_create_module
from server.app.blueprints.shop import create_module as shop_create_module
from server.app.cache import cache
from server.app.errors.error_handlers import error_handlers
from server.app.oauth import oauth
from server.database import db, migrate


def create_app(config = 'server.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app, origins=['http://localhost:8080', 'http://127.0.0.1:8080', 'http://192.168.0.6:8080'])
    error_handlers(app)

    @app.after_request
    def after_resquest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

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
        profile_create_module(app)

    return app
