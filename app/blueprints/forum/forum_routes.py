from app.blueprints.forum import forum
from flask import render_template
from database import db
from .models.post import Post
from .models.comment import Comment
from app.blueprints.auth.models.user import User


@forum.route('/')
def home():
    posts = Post.query.all()
    return render_template('forum.html', posts=posts)

