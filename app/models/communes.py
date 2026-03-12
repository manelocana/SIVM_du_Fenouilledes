



from app.extensions import db




class Commune(db.Model):

    __tablename__ = "communes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(255))