from app import db
from .user import User

class SavedExercise(db.Model):
    saved_exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500))
    calories_per_hour = db.Column(db.Float)
    total_calories = db.Column(db.Float)

    user = db.relationship("User", back_populates="saved_exercises")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))