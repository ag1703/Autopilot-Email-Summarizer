from datetime import datetime

from llm.ollama_client import ask_model
from utils.logger import logger


def ai_job():
    """
    Runs every scheduled interval.
    """
    logger.info("Scheduled job started.")

    print("=" * 50)
    print("Running Scheduled AI Job")
    print(datetime.now())

    response = ask_model(
        "Give me one motivational quote."
    )

    print(response)

    logger.info("AI Response: %s", response)

    print("=" * 50)