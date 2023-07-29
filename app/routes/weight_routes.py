from flask import Blueprint, request, jsonify, make_response, abort

weight_bp = Blueprint("weight", __name__, url_prefix="/users/<user_id>/weight")

@weight_bp.route("", methods=["GET"])
def index():
    return "Hello, Weight!"