import imaplib

from config.settings import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    IMAP_SERVER,
    IMAP_PORT,
)

from utils.logger import logger


class GmailClient:
    """
    Handles connection to Gmail using IMAP.
    """

    def __init__(self):
        self.mail = None

    def connect(self):
        """
        Connect to Gmail.
        """

        try:

            self.mail = imaplib.IMAP4_SSL(
                IMAP_SERVER,
                IMAP_PORT
            )

            self.mail.login(
                EMAIL_ADDRESS,
                EMAIL_PASSWORD
            )

            logger.info("Connected to Gmail.")

            print("Connected to Gmail successfully.")

        except Exception as e:

            logger.error(f"Gmail connection failed: {e}")

            raise

    def disconnect(self):
        """
        Close connection.
        """

        if self.mail:

            self.mail.logout()

            logger.info("Disconnected from Gmail.")

            print("Disconnected.")