from flask import Blueprint, request, jsonify, make_response, abort

food_bp = Blueprint("food", __name__, url_prefix="/users/<user_id>/food")

@food_bp.route("", methods=["GET"])
def index():
    return "Hello, food!"