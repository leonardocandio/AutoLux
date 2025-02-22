from flask import Flask
from flask_cors import CORS

from server.app.blueprints.forum import create_module as forum_create_module
from server.app.blueprints.users import create_module as users_create_module
from server.app.blueprints.shop import create_module as shop_create_module
from server.app.cache import cache
from server.app.errors.error_handlers import error_handlers
from server.app.oauth import oauth
from server.database import db, migrate


def create_app(config='server.config.Config'):
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

        shop_create_module(app)
        forum_create_module(app)
        users_create_module(app)

    return app
