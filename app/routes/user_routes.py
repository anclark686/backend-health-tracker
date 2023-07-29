from flask import Blueprint, request, jsonify, make_response, abort

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("", methods=["GET"])
def index():
    return "Hello, User!"