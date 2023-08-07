from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.weight import Weight
from .route_helpers import validate_model

weight_bp = Blueprint("weight", __name__, url_prefix="/users/<user_id>/weight")

@weight_bp.route("", methods=["GET"])
def index():
    return "Hello, Weight!"


# https://rapidapi.com/navii/api/bmi-calculator/