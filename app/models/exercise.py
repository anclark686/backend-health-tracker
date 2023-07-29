from app import db
from .user import User

class Exercise(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercise_name = db.Column(db.String(500))
    category = db.Column(db.String(100))
    calories_burned = db.Column(db.Float)
    date = db.Column(db.Date)

    user = db.relationship("User", back_populates="exercises")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
