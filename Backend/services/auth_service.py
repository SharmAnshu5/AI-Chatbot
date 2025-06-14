import jwt
from flask import request, jsonify, g
import os
from config import Config

SECRET_KEY = Config.SECRET_KEY

# Generate JWT token for a user
def generate_token(user_id):
    payload = {"user_id": user_id}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Middleware-like function to verify JWT
def verify_token():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authorization token is missing"}), 401

    if token.startswith("Bearer "):
        token = token.split(" ")[1]

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        g.user_id = decoded["user_id"]
        return None  # ✅ Token valid
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
