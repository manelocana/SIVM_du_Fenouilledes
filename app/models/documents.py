

from app.extensions import db
from sqlalchemy import func





class Document(db.Model):
    
    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    file = db.Column(db.String(255), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
