from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(50), nullable=False, unique=True)
    age = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(50))
    current_weight = db.Column(db.Float)
    goal_weight = db.Column(db.Float)
    bmi = db.Column(db.Float)
    est_water_intake_low = db.Column(db.Float)
    est_water_intake_high = db.Column(db.Float)
    est_base_calories = db.Column(db.Integer)
    est_goal_calories = db.Column(db.Integer)

    waters = db.relationship("Water", back_populates="user", lazy=True)
    weights = db.relationship("Weight", back_populates="user", lazy=True)
    exercises = db.relationship("Exercise", back_populates="user", lazy=True)
    foods = db.relationship("Food", back_populates="user", lazy=True)
    saved_exercises = db.relationship("SavedExercise", back_populates="user", lazy=True)
    saved_recipes = db.relationship("SavedRecipe", back_populates="user", lazy=True)
