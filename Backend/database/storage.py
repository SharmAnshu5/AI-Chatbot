import json
import os
from datetime import datetime

CHAT_HISTORY_FILE = "chat_history.json"

# Load existing history or initialize
if not os.path.exists(CHAT_HISTORY_FILE):
    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump({}, f)

# Save a new message to the session

def save_chat(session_id, user_message, bot_response):
    with open(CHAT_HISTORY_FILE, "r") as f:
        history = json.load(f)

    entry = history.get(session_id, [])
    timestamp = datetime.utcnow().isoformat()
    entry.append({"role": "user", "content": user_message, "timestamp": timestamp})
    entry.append({"role": "assistant", "content": bot_response, "timestamp": timestamp})

    history[session_id] = entry

    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# Get full session history

def get_chat_history(session_id):
    with open(CHAT_HISTORY_FILE, "r") as f:
        history = json.load(f)
    return history.get(session_id, [])
