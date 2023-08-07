from app import db
from .user import User

class SavedRecipe(db.Model):
    saved_recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500))
    ingredients = db.Column(db.Text(10000))
    servings = db.Column(db.String(500))
    instructions = db.Column(db.Text(10000))

    user = db.relationship("User", back_populates="saved_recipes")
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    @classmethod
    def from_dict(cls, user_id, data):
        pass

    def to_dict(self):
        pass
