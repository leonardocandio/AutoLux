from .shop_routes import shop


def create_module(app):
    app.register_blueprint(shop)
