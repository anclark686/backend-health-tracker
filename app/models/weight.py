from app import db
from .user import User

class Weight(db.Model):
    weight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weight_in_lbs = db.Column(db.Float)
    weight_in_kg = db.Column(db.Float)
    date = db.Column(db.Date)


    user = db.relationship("User", back_populates="weights")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def convert_to_kg(self):
        self.weight_in_kg = round(self.weight_in_lbs / 2.205, 2)
        return self.weight_in_kg