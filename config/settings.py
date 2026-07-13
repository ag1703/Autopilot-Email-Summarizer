import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# Ollama
# -------------------------------
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

# -------------------------------
# Database
# -------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

# -------------------------------
# Gmail
# -------------------------------
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_PORT = int(os.getenv("IMAP_PORT"))