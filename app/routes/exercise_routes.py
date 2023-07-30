from flask import Blueprint, request, jsonify, make_response, abort

exercise_bp = Blueprint("exercise", __name__, url_prefix="/users/<user_id>/exercise")

@exercise_bp.route("", methods=["GET"])
def index():
    return "Hello, Exercise!"

# https://api-ninjas.com/api/exercises
# https://api-ninjas.com/api/caloriesburned