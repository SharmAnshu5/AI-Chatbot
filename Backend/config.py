import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CORS_ORIGINS = ["http://localhost:3000"]
