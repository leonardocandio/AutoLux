from database import db
from app.utils.web_scraping_news import create_all_articles


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), default='No title')
    description = db.Column(db.String(900), default="No description")
    content = db.Column(db.String, default="No content")
    image_url = db.Column(db.String, default='https://coacademy-server-jc.com/uploads/courses/images/890.jpg')
    author = db.Column(db.String(120), default="No author")
    date_published = db.Column(db.DateTime, default="No date published")
    category = db.Column(db.String(255), default="No category")

    @staticmethod
    def get_news():
        if len(Article.query.all()) == 0:
            create_all_articles(db, Article)
