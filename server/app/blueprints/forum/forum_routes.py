import sqlalchemy
from flask import render_template, redirect, url_for, jsonify, request, abort
from flask_login import current_user, login_required

from server.app.blueprints.forum.controller import forum
from server.database import db
from .forms import PostForm, CommentForm
from .models.comment import Comment
from .models.post import Post
from ..auth.models.role import Permission

POSTS_PER_PAGE=20


def paginate(request, last_page=False):
    query = Post.query.order_by(Post.id)

    if last_page:
        page = query.count() // POSTS_PER_PAGE
    else:
        page = request.args.get('page', 1, type=int)

    return query.paginate(
        page=page, per_page=POSTS_PER_PAGE, error_out=True)


@forum.route('/')
def home():
    posts = paginate(request)
    return jsonify({
        'code': 200,
        'success': True,
        'posts': [post.format() for post in posts.items],
        'totalPosts': posts.total
    })


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


@forum.route('/<id>/create-comment', methods=['GET', 'POST'])
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
            "code" : 200,
            "body": comment.body,
            "img": comment.author.image_url,
            "author": comment.author.username,
            "last_updated": comment.last_updated.strftime("%Y-%m-%d")})
    except Exception as e:
        print(e)
        db.session.rollback()


@forum.route('/<id>/delete-comment', methods=['GET', 'POST'])
def delete_comment(id):
    try:
        comment = Comment.query.get_or_404(id)
        db.session.delete(comment)
        db.session.commit()
        success = True
    except Exception as e:
        success = False
        print(e)
        db.session.rollback()
    return jsonify({"success": success})


@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@forum.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
