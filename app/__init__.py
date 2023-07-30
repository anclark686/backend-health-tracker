from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    
    if test_config:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_TEST_DATABASE_URI")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
    
    # Import models here for Alembic setup
    from app.models.exercise import Exercise
    from app.models.food import Food
    from app.models.med import Med
    from app.models.saved_exercises import SavedExercise
    from app.models.saved_recipes import SavedRecipe
    from app.models.user import User
    from app.models.water import Water
    from app.models.weight import Weight

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes.routes import route_bp
    app.register_blueprint(route_bp)

    from .routes.exercise_routes import exercise_bp
    app.register_blueprint(exercise_bp)

    from .routes.food_routes import food_bp
    app.register_blueprint(food_bp)

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    from .routes.water_routes import water_bp
    app.register_blueprint(water_bp)

    from .routes.weight_routes import weight_bp
    app.register_blueprint(weight_bp)

    from .routes.med_routes import med_bp
    app.register_blueprint(med_bp)

    CORS(app)

    return app
