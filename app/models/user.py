import math
from datetime import datetime
from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(500))
    birthday = db.Column(db.String(100))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(50))
    height = db.Column(db.Integer)
    current_weight = db.Column(db.Float)
    goal_weight = db.Column(db.Float)
    activity_level = db.Column(db.String(100))
    bmi = db.Column(db.Float)
    est_water_intake = db.Column(db.Float)
    est_base_calories = db.Column(db.Integer)
    est_goal_calories = db.Column(db.Integer)

    waters = db.relationship("Water", back_populates="user", lazy=True)
    weights = db.relationship("Weight", back_populates="user", lazy=True)
    exercises = db.relationship("Exercise", back_populates="user", lazy=True)
    foods = db.relationship("Food", back_populates="user", lazy=True)
    meds = db.relationship("Med", back_populates="user", lazy=True)
    saved_exercises = db.relationship("SavedExercise", back_populates="user", lazy=True)
    saved_recipes = db.relationship("SavedRecipe", back_populates="user", lazy=True)

    @classmethod
    def from_dict(cls, data):
        age = cls.calc_age(data["birthday"])
        bmi = cls.calc_bmi(data["weight"], data["height"])
        water = cls.calc_water_intake(data["weight"])
        calories = cls.calc_calories(
            data["weight"],
            data["height"],
            age,
            data["loss"],
            data["sex"],
            data["activity"]
        )

        new_user = User(
            uid=data["uid"],
            name=data["name"],
            birthday=data["birthday"],
            age=age,
            sex=data["sex"],
            height=data["height"],
            current_weight=data["weight"],
            goal_weight=data["goal"],
            activity_level=data["activity"],
            bmi=bmi,
            est_water_intake=water,
            est_base_calories=calories[0],
            est_goal_calories=calories[1],
        )

        return new_user

    def to_dict(self):
        user_data = {
            "id": self.user_id,
            "uid": self.uid,
            "name": self.name,
            "birthday": self.birthday,
            "age": self.calc_age(self.birthday),
            "sex": self.sex,
            "height": self.height,
            "weight": self.current_weight,
            "goal": self.goal_weight,
            "activity": self.activity_level,
            "bmi": self.bmi,
            "water": self.est_water_intake,
            "requirement": self.est_base_calories,
            "calories": self.est_goal_calories
        }

        return user_data
    
    @classmethod
    def calc_age(cls, birthday):
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - \
            ((today.month, today.day) < (birth_date.month, birth_date.day))

        return age
    
    @classmethod
    def calc_water_intake(cls, weight):
        return round(weight / 2, 2)

    @classmethod
    def calc_calories(cls, weight, height, age, lbs_per_week, sex, activity):
        # men: (4.536 × weight in pounds) + (15.88 × height in inches) 
        # - (5 × age) + 5
        # women: (4.536 × weight in pounds) + (15.88 × height in inches) 
        # - (5 × age) - 161
        if sex == "male":
            bmr = round((4.536 * weight) + (15.88 * height) - (5 * age) + 5, 2)
        elif sex == "female":
            bmr = round((4.536 * weight) + (15.88 * height) - (5 * age) - 161, 2)

        if activity == "sedentary":
            requirement = round(bmr * 1.2, 2)
        elif activity == "light":
            requirement = round(bmr * 1.375, 2)
        elif activity == "moderate":
            requirement = round(bmr * 1.55, 2)
        elif activity == "very":
            requirement = round(bmr * 1.725, 2)
        else:
            requirement = round(bmr * 1.9, 2)

        goal = round(requirement - (500 * lbs_per_week), 2)
        return (requirement, goal)

    @classmethod
    def calc_bmi(cls, weight, height):
        # (w ÷ h2) * 703
        return round(703 * (weight / math.pow(height, 2)), 2)

