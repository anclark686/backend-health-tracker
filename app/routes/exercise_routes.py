from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.exercise import Exercise
from .route_helpers import validate_model

exercise_bp = Blueprint("exercise", __name__, url_prefix="/users/<user_id>/exercise")

@exercise_bp.route("", methods=["GET"])
def index():
    return "Hello, Exercise!"

# https://api-ninjas.com/api/exercises
# https://api-ninjas.com/api/caloriesburned