from .forum_routes import forum


def create_module(app):
    app.register_blueprint(forum)
