from flask import render_template, abort
from flask_login import current_user, login_required
from server.app.blueprints.news.controller import news
from .models.article import Article
from ..auth.models.role import Permission


@news.route('/', methods=['GET', 'POST'])
def home():
    articles = Article.query.all()
    return render_template('news.html', articles=articles)


@news.route('/<newid>', methods=['GET', 'POST'])
def article_page(newid):
    article = Article.query.get(newid)
    return render_template('see_more_news.html', article=article)


@news.route('/add_news')
def add_news():
    return 'add news'


@news.route('/delete_news')
def delete_news():
    return 'delete news'


@news.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@news.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
