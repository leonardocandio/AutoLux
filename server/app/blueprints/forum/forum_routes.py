from datetime import datetime

from flask import jsonify, request, abort
from flask_login import current_user, login_required

from server.app.blueprints.forum.controller import forum
from .models.comment import Comment
from .models.post import Post
from ..auth.models.role import Permission

ITEMS_PER_PAGE = 20


def paginate(model, request, last_page=False):
    query = Post.query.order_by(model.created_at.desc())

    if last_page:
        page = query.count() // ITEMS_PER_PAGE
    else:
        page = request.args.get('page', 1, type=int)

    return query.paginate(
        page=page, per_page=ITEMS_PER_PAGE, error_out=True)


@forum.route('/', methods=['GET'])
def get_forum():
    posts = paginate(Post, request)
    return jsonify({
        'code': 200,
        'success': True,
        'posts': [post.format() for post in posts.items],
        'total_posts': posts.total
    })


@forum.route('/', methods=['POST'])
def create_post():
    body = request.get_json()
    post_body = body.get('post_body', None)
    post_title = body.get('post_title', None)

    if current_user.can(Permission.WRITE_ARTICLES):
        post = Post(title=post_body, body=post_title, author=current_user._get_current_object())
        try:
            post.insert()
        except Exception:
            abort(500)

        posts = paginate(Post, request)
    return jsonify({
        'code': 200,
        'success': True,
        'post_created': post.id,
        'posts': [post.format() for post in posts.items],
        'total_posts': posts.total
    })


@forum.route('/', methods=['DELETE'])
def delete_post():
    body = request.get_json()
    post_id = body.get('post_id', None)
    post = Post.query.get_or_404(post_id)
    if current_user.can(Permission.WRITE_ARTICLES and current_user.id == post.author_id):
        try:
            post.delete()
        except Exception:
            abort(500)
        posts = paginate(Post, request)
        return jsonify({
            'code': 200,
            'success': True,
            'posts': [post.format() for post in posts.items],
            'total_posts': posts.total
        })
    else:
        abort(403)

@forum.route('/', methods=['PATCH'])
def update_post():
    body = request.get_json()
    post_id = body.get('post_id', None)
    post_body = body.get('post_body', None)
    post_title = body.get('post_title', None)
    post = Post.query.get_or_404(post_id)
    if current_user.can(Permission.WRITE_ARTICLES and current_user.id == post.author_id):
        try:
            post.body = post_body
            post.title = post_title
            post.last_updated = datetime.utcnow
            post.update()
        except Exception:
            abort(500)
        posts = paginate(Post, request)
        return jsonify({
            'code': 200,
            'success': True,
            'posts': [post.format() for post in posts.items],
            'total_posts': posts.total
        })
    else:
        abort(403)


@forum.route('/<id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    comments = paginate(Comment, request)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'author_id': post.author_id,
        'last_updated': post.last_updated,
        'created_at': post.created_at,
        'comments': [comment.format() for comment in comments.items]})


@forum.route('/<id>', methods=['POST'])
def create_comment(id):
    post = Post.query.get_or_404(id)
    body = request.get_json()
    comment_body = body.get('comment_body', None)
    comment_author = current_user._get_current_object()
    try:
        comment = Comment(body=comment_body, post=post, author=comment_author)
        comment.insert()
        return jsonify({
            "code": 200,
            "body": comment.body,
            "img": comment.author.image_url,
            "author": comment.author.username,
            "last_updated": comment.last_updated.strftime("%Y-%m-%d")})
    except Exception as e:
        print(e)


@forum.route('/<id>', methods=['DELETE'])
def delete_comment(id):
    body = request.get_json()
    comment_id = body.get('comment_id', None)
    comment = Comment.query.get_or_404(comment_id)
    if current_user.can(Permission.WRITE_ARTICLES and current_user.id == comment.author_id):
        try:
            comment.delete()
        except Exception:
            abort(500)
        comments = paginate(Comment, request)
        return jsonify({
            'code': 200,
            'success': True,
            'comments': [comment.format() for comment in comments.items],
            'total_comments': comments.total
        })
    else:
        abort(403)


@forum.route('/<id>', methods=['PATCH'])
def update_comment(id):
    body = request.get_json()
    comment_id = body.get('comment_id', None)
    comment_body = body.get('comment_body', None)
    comment = Comment.query.get_or_404(comment_id)
    if current_user.can(Permission.WRITE_ARTICLES and current_user.id == comment.author_id):
        try:
            comment.body = comment_body
            comment.last_updated = datetime.utcnow
            comment.update()
        except Exception:
            abort(500)
        comments = paginate(Comment, request)
        return jsonify({
            'code': 200,
            'success': True,
            'comments': [comment.format() for comment in comments.items],
            'total_comments': comments.total
        })
    else:
        abort(403)


@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@forum.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
