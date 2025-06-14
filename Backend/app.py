from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from services.logging_service import log_request_response
from routes.auth_routes import auth_bp
from routes.chat_routes import chat_bp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

log_request_response(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)

@app.route("/", methods=["GET"])
def root():
    return {"status": "Chatbot Backend is running."}, 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
