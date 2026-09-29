import ollama

from config.settings import OLLAMA_MODEL
from utils.logger import logger
from utils.retry import retry_with_backoff

from exceptions.custom_exceptions import (
    SummarizationError
)


def summarize_email(email_data):
    """
    Sends the cleaned email to Ollama and returns a summary.
    Retries the Ollama request up to three times if it fails.
    """

    prompt = f"""
You are an AI assistant.

Summarize the following email in 3–5 bullet points.

Subject:
{email_data["subject"]}

From:
{email_data["from"]}

Body:
{email_data["body"]}
"""

    def call_ollama():

        return ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    try:

        response = retry_with_backoff(
            call_ollama,
            operation_name="Ollama summarization"
        )

        summary = response["message"]["content"]

        logger.info("Email summarized successfully.")

        return summary

    except Exception as e:

        logger.error(
            f"Ollama summarization failed after retries: {e}"
        )

        raise SummarizationError(
            "Failed to summarize email."
        )