from flask import Blueprint, request, jsonify, make_response, abort

med_bp = Blueprint("meds", __name__, url_prefix="/users/<user_id>/meds")

@med_bp.route("", methods=["GET"])
def index():
    return "Hello, med!"

# https://lhncbc.nlm.nih.gov/RxNav/APIs/api-Interaction.findDrugInteractions.html
