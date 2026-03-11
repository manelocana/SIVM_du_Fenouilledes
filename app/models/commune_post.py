


from app.extensions import db




class CommunePost(db.Model):

    __tablename__ = "commune_posts"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    image = db.Column(db.String(255))

    section = db.Column(db.String(20))  # sivm / aci

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    commune_id = db.Column(
        db.Integer,
        db.ForeignKey("communes.id"),
        nullable=False
    )