from app import db
from .user import User

class Water(db.Model):
    water_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

    user = db.relationship("User", back_populates="waters")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))