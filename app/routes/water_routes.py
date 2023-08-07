from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.water import Water
from .route_helpers import validate_model

water_bp = Blueprint("water", __name__, url_prefix="/users/<user_id>/water")

@water_bp.route("", methods=["GET"])
def index():
    return "Hello, Water!"