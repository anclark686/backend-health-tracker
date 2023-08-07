# https://api-ninjas.com/api/recipe
from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.food import Food
from .route_helpers import validate_model

food_bp = Blueprint("food", __name__, url_prefix="/users/<user_id>/food")


@food_bp.route("", methods=["GET"])
def get_users_foods(user_id):
    user = validate_model(User, user_id)
    food_response = [food.to_dict() for food in user.foods]

    return make_response(jsonify(food_response), 200)


@food_bp.route("", methods=["POST"])
def create_food(user_id):
    print(user_id)
    request_body = request.get_json()
    print(request_body)

    try:
        new_food = Food.from_dict(request_body)
    except KeyError:
        abort(make_response(jsonify({"details": "Invalid data"}), 400))

    db.session.add(new_food)
    db.session.commit()

    return make_response(jsonify(new_food.to_dict()), 201)

