from .home_routes import home


def create_module(app):
    app.register_blueprint(home)
