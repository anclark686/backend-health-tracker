from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy.exc import IntegrityError
from app import db
from app.models.user import User
from .route_helpers import validate_model

user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("", methods=["GET"])
def get_user_by_uid_or_all_users():
    users = User.query.all()
    users_response = [user.to_dict() for user in users]

    return make_response(jsonify(users_response), 200)


@user_bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()

    try:
        new_user = User.from_dict(request_body)
        db.session.add(new_user)
        db.session.commit()
    except KeyError as err:
        print(err)
        abort(make_response(jsonify({"details": "Invalid data"}), 400))
    except IntegrityError as err:
        db.session.rollback()
        print(err)
        abort(make_response(jsonify({"details": "Duplicate UID"}), 400))

    return make_response(jsonify(new_user.to_dict()), 201)


@user_bp.route("/<user_uid>", methods=["GET"])
def get_one_user(user_uid):
    try:
        user = User.query.filter_by(uid=user_uid).one()
        return make_response(jsonify(user.to_dict()), 200)
    except: 
        abort(make_response({"message": f"user with uid {user_uid} was not found."}, 404))


@user_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    user = validate_model(User, user_id)

    req_body = request.get_json()

    age = User.calc_age(req_body["birthday"])
    bmi = User.calc_bmi(req_body["weight"], req_body["height"])
    water = User.calc_water_intake(req_body["weight"])
    calories = User.calc_calories(
        req_body["weight"],
        req_body["height"],
        age,
        req_body["loss"],
        req_body["sex"],
        req_body["activity"]
    )

    user.age = age
    user.name = req_body["name"]
    user.height = req_body["height"]
    user.current_weight = req_body["weight"]
    user.goal_weight = req_body["goal"]
    user.activity_level = req_body["activity"]
    user.bmi = bmi
    user.est_water_intake = water
    user.est_base_calories = calories[0]
    user.est_goal_calories = calories[1]

    db.session.commit()

    return make_response(jsonify({"user": user.to_dict()}), 200)
