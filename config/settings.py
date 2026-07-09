from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
DATABASE_URL = os.getenv("DATABASE_URL")