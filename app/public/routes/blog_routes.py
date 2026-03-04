

from flask import Blueprint, render_template
from app.models.post import Post

from app.models.settings import Setting
from app.extensions import db



blog_bp = Blueprint('blog', __name__)



@blog_bp.route('/blog')
def blog():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    setting = Setting.query.first()
    if not setting:
        setting = Setting()
        db.session.add(setting)
        db.session.commit()

    return render_template('public/blog/blog.html', posts=posts, setting=setting)