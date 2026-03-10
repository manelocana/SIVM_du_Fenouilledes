

from flask import Blueprint, render_template
from app.models.post import Post

from app.models.settings import Setting
from app.extensions import db

from app.models.documents import Document



blog_bp = Blueprint('blog', __name__)



@blog_bp.route('/blog')
def blog():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    setting = Setting.query.first()
    if not setting:
        setting = Setting()
        db.session.add(setting)
        db.session.commit()

    lettres = Document.query.filter_by(category="lettre").all()
    deliberations = Document.query.filter_by(category="deliberation").all()
    arretes = Document.query.filter_by(category="arrete").all()

    return render_template('public/blog/blog.html', 
                           posts=posts, 
                           setting=setting, 
                           lettres=lettres, 
                           deliberations=deliberations, 
                           arretes=arretes
                           )