import requests

from config.settings import SLACK_WEBHOOK_URL
from utils.logger import logger
from utils.retry import retry_with_backoff

from exceptions.custom_exceptions import (
    SlackNotificationError
)


def post_to_slack(message):
    """
    Sends a message to Slack using the Incoming Webhook.
    Retries the request up to three times if it fails.
    """

    payload = {
        "text": message
    }

    def send_message():

        response = requests.post(
            SLACK_WEBHOOK_URL,
            json=payload,
            timeout=10
        )

        response.raise_for_status()

    try:

        retry_with_backoff(
            send_message,
            operation_name="Slack notification"
        )

        logger.info(
            "Message sent to Slack successfully."
        )

        print(
            "Message sent to Slack successfully."
        )

    except Exception as e:

        logger.error(
            f"Slack notification failed after retries: {e}"
        )

        raise SlackNotificationError(
            "Failed to send Slack notification."
        )