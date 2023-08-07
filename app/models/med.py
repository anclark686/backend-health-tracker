from app import db
from .user import User

class Med(db.Model):
    med_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    med_name = db.Column(db.String(500))
    time_needed = db.Column(db.String(100))
    last_taken = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)
    date = db.Column(db.String(100))

    user = db.relationship("User", back_populates="meds")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    @classmethod
    def from_dict(cls, user_id, data):
        pass

    def to_dict(self):
        pass
