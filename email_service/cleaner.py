from bs4 import BeautifulSoup
import html
import re

from utils.logger import logger


def clean_email(text):
    """
    Cleans HTML email content for LLM processing.
    """

    if not text:
        return ""

    try:
        # Decode HTML entities
        text = html.unescape(text)

        # Remove HTML tags
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text()

        # Replace multiple whitespace (spaces, tabs, newlines) with a single space
        text = re.sub(r"\s+", " ", text)

        # Remove leading/trailing spaces
        text = text.strip()

        logger.info("Email cleaned successfully.")

        return text

    except Exception as e:
        logger.error(f"Email cleaning failed: {e}")
        raise