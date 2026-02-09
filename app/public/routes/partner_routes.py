

from flask import Blueprint, render_template


partner_bp = Blueprint('partner', __name__)



@partner_bp.route('/partner')
def partner():
    return render_template('public/partner/partner.html')