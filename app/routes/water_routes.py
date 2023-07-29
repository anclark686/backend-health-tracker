from flask import Blueprint, request, jsonify, make_response, abort

water_bp = Blueprint("water", __name__, url_prefix="/users/<user_id>/water")

@water_bp.route("", methods=["GET"])
def index():
    return "Hello, Water!"