from flask import Blueprint

route_bp = Blueprint("routes", __name__, url_prefix="/")

@route_bp.route("", methods=["GET"])
def index():
    return "Financial planner backend - frontend is at http://localhost:5173"