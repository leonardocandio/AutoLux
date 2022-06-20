from .news_routes import news


def create_module(app):
    app.register_blueprint(news)
