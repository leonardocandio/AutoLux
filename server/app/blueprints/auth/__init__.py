from flask_login import LoginManager

from .auth_routes import auth
from .models.user import AnonymousUser

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(userid):
    from server.app.blueprints.auth.models.user import User
    return User.query.get(int(userid))


def create_module(app):
    login_manager.init_app(app)
    app.register_blueprint(auth)
