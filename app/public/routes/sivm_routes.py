

from flask import Blueprint, render_template

from app.models.communes import Commune
from app.models.commune_post import CommunePost





sivm_bp = Blueprint('sivm', __name__)



@sivm_bp.route('/sivm')
def sivm():
    communes = Commune.query.order_by(Commune.name).all()
    return render_template('public/sivm/sivm.html', communes=communes)




@sivm_bp.route("/sivm/<int:commune_id>")
def sivm_commune(commune_id):

    commune = Commune.query.get_or_404(commune_id)

    posts = CommunePost.query.filter_by(
        commune_id=commune_id,
        section="sivm"
    ).order_by(
        CommunePost.created_at.desc()
    ).all()

    return render_template(
        "public/sivm/commune.html",
        commune=commune,
        posts=posts
    )