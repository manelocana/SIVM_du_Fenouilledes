

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required
from app.decorators import role_required

from app.models.documents import Document
from app.extensions import db

from app.forms.documents import DocumentForm

from app.utils.files import save_file, delete_file





documents_admin_bp = Blueprint("documents_admin", __name__, url_prefix="/admin/documents")



@documents_admin_bp.route("/")
@login_required
@role_required(["admin"])
def documents_list():
    documents = Document.query.order_by(Document.created_at.desc()).all()

    return render_template("admin/documents/documents_list.html", documents=documents)



@documents_admin_bp.route("/new", methods=["GET","POST"])
@login_required
@role_required(["admin"])
def document_new():

    form = DocumentForm()

    if form.validate_on_submit():

        file = form.file.data
        filename = save_file(file, "documents")

        doc = Document(
            title=form.title.data,
            category=form.category.data,
            file=filename
        )

        db.session.add(doc)
        db.session.commit()

        flash("Document enregistré", "success")

        return redirect(url_for("documents_admin.documents_list"))

    return render_template(
        "admin/documents/documents_new.html",
        form=form
    )




@documents_admin_bp.route("/<int:id>/edit", methods=["GET","POST"])
@login_required
@role_required(["admin"])
def document_edit(id):

    doc = Document.query.get_or_404(id)

    form = DocumentForm(obj=doc)

    form.file.data = None

    if form.validate_on_submit():

        doc.title = form.title.data
        doc.category = form.category.data

        file = form.file.data

        if file and file.filename:
            delete_file(doc.file, "documents")
            doc.file = save_file(file, "documents")

        db.session.commit()

        flash("Document updated", "success")

        return redirect(url_for("documents_admin.documents_list"))

    return render_template(
        "admin/documents/documents_edit.html",
        form=form,
        doc=doc
    )




@documents_admin_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
@role_required(["admin"])
def document_delete(id):

    doc = Document.query.get_or_404(id)

    delete_file(doc.file, "documents")

    db.session.delete(doc)
    db.session.commit()

    flash("Document deleted", "danger")

    return redirect(url_for("documents_admin.documents_list"))