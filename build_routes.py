from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from services.compatibility_service import check_compatibility

build = Blueprint("build", __name__)

@build.route("/check", methods=["POST"])
def check():
    data = request.json
    return jsonify(check_compatibility(data))