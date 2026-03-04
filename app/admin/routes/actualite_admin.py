


from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required
from app.decorators import role_required

from app.models.settings import Setting
from app.models.info_card import InfoCard
from app.models.post import Post

from app.extensions import db

from app.forms.date import SettingDateForm




actualite_admin_bp = Blueprint("actualite_admin", __name__, url_prefix="/admin/actualite")


@actualite_admin_bp.route("/")
@login_required
@role_required(["admin"])
def actualite_dashboard():
    setting = Setting.query.first()
    cards = InfoCard.query.all()
    posts = Post.query.order_by(Post.created_at.desc()).all()

    return render_template(
        "admin/administration/actualite_dashboard.html",
        setting=setting,
        cards=cards,
        posts=posts
    )



@actualite_admin_bp.route("/admin/setting_date", methods=["GET", "POST"])
@login_required
@role_required(["admin"])
def edit_setting_date():
    setting = Setting.query.first()
    form = SettingDateForm(obj=setting)  # Pre-llenar con la fecha actual

    if form.validate_on_submit():
        setting.next_meeting_date = form.next_meeting_date.data
        db.session.commit()
        flash("Fecha actualizada", "success")
        return redirect(url_for("actualite_admin.edit_setting_date"))

    return render_template("admin/administration/setting_date.html", form=form)