


from app.extensions import db



class InfoCard(db.Model):
    
    __tablename__ = "info_card"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    file_url = db.Column(db.String(255))