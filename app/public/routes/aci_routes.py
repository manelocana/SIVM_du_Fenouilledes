

from flask import Blueprint, render_template

from app.models.communes import Commune
from app.models.commune_post import CommunePost





aci_bp = Blueprint('aci', __name__)



@aci_bp.route('/aci')
def aci():
    communes = Commune.query.order_by(Commune.name).all()
    return render_template('public/aci/aci.html', communes=communes)




@aci_bp.route("/aci/<int:commune_id>")
def aci_commune(commune_id):

    commune = Commune.query.get_or_404(commune_id)

    posts = CommunePost.query.filter_by(
        commune_id=commune_id,
        section="aci"
    ).order_by(
        CommunePost.created_at.desc()
    ).all()

    return render_template(
        "public/aci/commune.html",
        commune=commune,
        posts=posts
    )