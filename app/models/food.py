from app import db
from .user import User

class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_name = db.Column(db.String(500))
    meal = db.Column(db.String(100))
    amount = db.Column(db.String(500))
    calories = db.Column(db.Float)
    date = db.Column(db.Date)

    user = db.relationship("User", back_populates="foods")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
