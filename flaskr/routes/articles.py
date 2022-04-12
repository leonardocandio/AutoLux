from flask import Blueprint, render_template
from models.article import Article
from utils.db import db

news = Blueprint('news', __name__)

@news.route('/news_list', methods=['GET', 'POST'])
def news_list():
    articles = Article.query.all()
    return render_template('news.html', articles=articles)

@news.route('/add_news')
def add_news():
    return 'add news'

@news.route('/delete_news')
def delete_news():
    return 'delete news'