from flask import render_template, redirect, url_for
from flask_login import current_user

from app.blueprints.forum.controller import forum
from database import db
from .forms import PostForm
# noinspection PyUnresolvedReferences
from .models.comment import Comment
from .models.post import Post
from ..auth.models.role import Permission


@forum.route('/')
def home():
    posts = Post.query.order_by("publish_date").all()

    return render_template('forum.html', posts=posts)


@forum.route("/publish")
def publish():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user.id)
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)

        return redirect(url_for("forum.home"))
    return url_for("forum.publish")


@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
