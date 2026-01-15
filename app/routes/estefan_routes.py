

from flask import Blueprint, render_template



estefan_bp = Blueprint('estefan', __name__)



@estefan_bp.route('/estefan')
def estefan():
    return render_template('estefan/estefan.html')