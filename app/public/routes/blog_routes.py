

from flask import Blueprint, render_template
from app.models.post import Post

from app.models.settings import Setting
from app.extensions import db

from app.models.documents import Document



blog_bp = Blueprint('blog', __name__, url_prefix='/blog')




@blog_bp.route('/list')
def blog_list():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('public/blog/blog_list.html', posts=posts)




@blog_bp.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("public/blog/blog_post.html", post=post)




@blog_bp.route('/')
def blog():
    last_post = Post.query.order_by(Post.created_at.desc()).first()
    setting = Setting.query.first()
    if not setting:
        setting = Setting()
        db.session.add(setting)
        db.session.commit()

    lettres = Document.query.filter_by(category="lettre").order_by(Document.created_at.desc()).limit(1).all()
    deliberations = Document.query.filter_by(category="deliberation").order_by(Document.created_at.desc()).limit(1).all()
    arretes = Document.query.filter_by(category="arrete").order_by(Document.created_at.desc()).limit(1).all()

    return render_template('public/blog/blog.html', 
                           last_post=last_post, 
                           setting=setting, 
                           lettres=lettres, 
                           deliberations=deliberations, 
                           arretes=arretes
                           )





@blog_bp.route('/documents/lettres')
def lettres_list():
    lettres = Document.query.filter_by(category="lettre").order_by(Document.created_at.desc()).all()
    return render_template("public/documents/lettres_list.html", lettres=lettres)



@blog_bp.route('/documents/deliberations')
def deliberations_list():
    deliberations = Document.query.filter_by(category="deliberation").order_by(Document.created_at.desc()).all()
    return render_template("public/documents/deliberations_list.html", deliberations=deliberations)



@blog_bp.route('/documents/arretes')
def arretes_list():
    arretes = Document.query.filter_by(category="arrete").order_by(Document.created_at.desc()).all()
    return render_template("public/documents/arretes_list.html", arretes=arretes)