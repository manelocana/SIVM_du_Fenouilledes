

from flask import Blueprint, render_template


julien_bp = Blueprint('julien', __name__)


@julien_bp.route('/julien')
def julien():
    return render_template('julien/julien.html')