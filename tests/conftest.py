import pytest
from app import create_app
from app import db
from flask.signals import request_finished

from app.models.exercise import Exercise
from app.models.food import Food
from app.models.med import Med
from app.models.saved_exercises import SavedExercise
from app.models.saved_recipes import SavedRecipe
from app.models.user import User
from app.models.water import Water
from app.models.weight import Weight


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
