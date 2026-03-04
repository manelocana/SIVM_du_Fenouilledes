

from app.extensions import db
from datetime import datetime
from sqlalchemy.sql import func



class Post(db.Model):
    
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    published = db.Column(db.Boolean, default=True)