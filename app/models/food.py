from app import db
from .user import User

class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_name = db.Column(db.String(500))
    meal = db.Column(db.String(100))
    amount = db.Column(db.String(500))
    calories = db.Column(db.Float)
    date = db.Column(db.String(100))

    user = db.relationship("User", back_populates="foods")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    @classmethod
    def from_dict(cls, user_id, data):
        new_food = Food(
            food_name=data["name"],
            amount=data["amount"],
            calories=data["calories"],
            meal=data["meal"],
            date=data["date"],
            user_id=user_id
        )

        return new_food

    def to_dict(self):
        food_data = {
            "id": self.food_id,
            "name": self.food_name,
            "amount": self.amount,
            "calories": self.calories,
            "meal": self.meal,
            "date": self.date,
            "user": self.user_id
        }

        return food_data
