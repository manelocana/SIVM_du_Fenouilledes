

from flask import Blueprint, render_template
from app.models.post import Post



blog_bp = Blueprint('blog', __name__)



@blog_bp.route('/blog')
def blog():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('public/blog/blog.html', posts=posts)