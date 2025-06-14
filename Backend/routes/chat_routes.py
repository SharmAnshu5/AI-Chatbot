from flask import Blueprint, request, jsonify
from services.chat_service import preprocess, get_openai_response
from services.auth_service import verify_token
from database.storage import save_chat, get_chat_history
import uuid

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    auth_error = verify_token()
    if auth_error:
        return auth_error

    try:
        data = request.get_json()
        session_id = data.get("session_id") or str(uuid.uuid4())
        user_message = data.get("message", "")

        cleaned_input = preprocess(user_message)
        prompt = f"Human: {cleaned_input}\nAI:"
        bot_response = get_openai_response(prompt)

        save_chat(session_id, user_message, bot_response)

        return jsonify({"session_id": session_id, "response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route("/history/<session_id>", methods=["GET"])
def history(session_id):
    auth_error = verify_token()
    if auth_error:
        return auth_error

    try:
        history = get_chat_history(session_id)
        return jsonify({"history": history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
