from .profile_routes import profile


def create_module(app):
    app.register_blueprint(profile)
