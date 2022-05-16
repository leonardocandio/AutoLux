import sqlalchemy
from flask import render_template, redirect, url_for, jsonify, request, abort
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
    validate = False
    if form.validate_on_submit():
        validate = True
    expression = sqlalchemy.sql.expression.desc("last_updated")
    comments = post_q.comments.order_by(expression)
    return render_template("post.html", posts=[post_q], form=form, comments=comments, validate=validate)


@forum.route('/<id>/create_comment', methods=['GET', 'POST'])
def create_comment(id):
    post_q = Post.query.get_or_404(id)
    body = request.get_json()
    body = body["comment-body"]
    author = current_user._get_current_object()
    try:
        comment = Comment(body=body, post=post_q, author=author)
        db.session.add(comment)
        db.session.commit()
        return jsonify({
            "body": comment.body,
            "author": comment.author.username,
            "last_updated": comment.last_updated})
    except Exception as e:
        print(e)
        db.session.rollback()


@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@forum.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
