from datetime import datetime

from flask import jsonify, request, abort
from flask_login import current_user, login_required

from server.app.blueprints.forum.controller import forum
from server.app.blueprints.users.models.role import Permission
from .models.comment import Comment
from .models.post import Post

ITEMS_PER_PAGE = 20


def paginate(model, request, last_page=False):
    query = model.query.order_by(model.created_at.desc())

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
@login_required
def create_post():
    body = request.get_json()
    post_body = body.get('post_body', None)
    post_title = body.get('post_title', None)

    post = Post(title=post_title, body=post_body, author=current_user._get_current_object())
    try:
        post.insert()
    except Exception:
        abort(500)
    print(post.format())
    posts = paginate(Post, request)

    return jsonify({
        'code': 200,
        'success': True,
        'post_created': post.id,
        'posts': [post.format() for post in posts.items],
        'total_posts': posts.total
    })


@forum.route('/', methods=['DELETE'])
@login_required
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
            'post_deleted': post_id,
            'posts': [post.format() for post in posts.items],
            'total_posts': posts.total
        })
    else:
        abort(403)


@forum.route('/', methods=['PATCH'])
@login_required
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
            'post_updated': post_id,
            'posts': [post.format() for post in posts.items],
            'total_posts': posts.total
        })
    else:
        abort(403)


@forum.route('/<id>', methods=['GET'])
@login_required
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({
        'code': 200,
        'success': True,
        'post': post.format()
    })


@forum.route('/<id>', methods=['POST'])
@login_required
def create_comment(id):
    post = Post.query.get_or_404(id)
    body = request.get_json()
    comment_body = body.get('comment_body', None)
    comment_author = current_user._get_current_object()
    try:
        comment = Comment(body=comment_body, post=post, author=comment_author)
        comment.insert()
    except Exception:
        abort(500)
    comments = post.comments.all()
    return jsonify({
        'code': 200,
        'success': True,
        'comment_created': comment.id,
        'comments': [comment.format() for comment in comments],
        'total_comments': len(comments)
    })


@forum.route('/<id>', methods=['DELETE'])
@login_required
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
            'comment_deleted': comment_id,
            'comments': [comment.format() for comment in comments.items],
            'total_comments': comments.total
        })
    else:
        abort(403)


@forum.route('/<id>', methods=['PATCH'])
@login_required
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
            'comment_updated': comment_id,
            'comments': [comment.format() for comment in comments.items],
            'total_comments': comments.total
        })
    else:
        abort(403)


@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
