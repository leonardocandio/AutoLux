import sqlalchemy
from flask import render_template, redirect, url_for, jsonify
from flask_login import current_user, login_required

from app.blueprints.forum.controller import forum
from database import db
from .forms import PostForm, CommentForm
# noinspection PyUnresolvedReferences
from .models.comment import Comment
from .models.post import Post
from ..auth.models.role import Permission


@forum.route('/')
def home():
    expression = sqlalchemy.sql.expression.desc("created_at")
    posts = Post.query.order_by(expression).all()

    return render_template('forum.html', posts=posts)


@forum.route("/publish", methods=['GET', 'POST'])
@login_required
def publish():
    form = PostForm()
    if form.validate_on_submit() and current_user.can(Permission.WRITE_ARTICLES):
        post = Post(title=form.title.data, body=form.body.data, author=current_user._get_current_object())
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)

        return redirect(url_for("forum.home"))
    return render_template("publish.html", form=form)


@forum.route('/<id>', methods=['GET', 'POST'])
def post(id):
    post_q = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post_q, author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        return jsonify({"id": comment.id,
                        "body": comment.body,
                        "author": comment.author.username,
                        "last_updated": comment.last_updated})
    comments = post_q.comments
    return render_template("post.html", posts=[post_q], form=form, comments=comments)


@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
