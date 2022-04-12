from utils.db import db

# Cada notica tiene title, description, content, image_url, author, date_published, category
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), default='No title')
    description = db.Column(db.String(900), default="No description")
    content = db.Column(db.String, default="No content")
    image_url = db.Column(db.String, default="No image")
    author = db.Column(db.String(120), default="No author")
    date_published = db.Column(db.DateTime, default="No date published")
    category = db.Column(db.String(255), default="No category")
