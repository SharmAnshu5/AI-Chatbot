from flask import Blueprint, request, jsonify
from services.auth_service import generate_token
import uuid

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user_id = data.get("user_id", str(uuid.uuid4()))
    token = generate_token(user_id)
    return jsonify({"token": token})
