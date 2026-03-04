

from app.extensions import db



class Setting(db.Model):
    __tablename__ = "setting"

    id = db.Column(db.Integer, primary_key=True)
    next_meeting_date = db.Column(db.Date, nullable=True)