from flask import render_template, abort
from .models.article import Article
from app.blueprints.news import news

@news.route('/', methods=['GET', 'POST'])
def home():
    articles = Article.query.all()
    return render_template('news.html', articles=articles)


@news.route('/add_news')
def add_news():
    return 'add news'


@news.route('/delete_news')
def delete_news():
    return 'delete news'
