import imaplib

from config.settings import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    IMAP_SERVER,
    IMAP_PORT,
)

from utils.logger import logger

from exceptions.custom_exceptions import (
    EmailConnectionError,
    EmailFetchError
)


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

            raise EmailConnectionError(
                "Unable to connect to Gmail."
            )

    def disconnect(self):
        """
        Close connection.
        """

        if self.mail:

            self.mail.logout()

            logger.info("Disconnected from Gmail.")

            print("Disconnected.")

    def open_inbox(self):
        """
        Opens the inbox.
        """

        try:

            status, _ = self.mail.select("INBOX")

            if status != "OK":
                raise EmailFetchError(
                    "Unable to open inbox."
                )

            logger.info("Inbox opened.")

        except Exception as e:

            logger.error(f"Failed to open inbox: {e}")

            raise EmailFetchError(
                "Unable to open inbox."
            )

    def search_unread(self):
        """
        Returns unread email IDs.
        """

        try:

            status, messages = self.mail.search(None, "UNSEEN")

            if status != "OK":

                logger.warning("Failed to search unread emails.")

                return []

            email_ids = messages[0].split()

            logger.info(f"Unread emails found: {len(email_ids)}")

            return email_ids

        except Exception as e:

            logger.error(f"Failed to search unread emails: {e}")

            raise EmailFetchError(
                "Unable to search unread emails."
            )

    def fetch_email(self, email_id):
        """
        Downloads one email.
        """

        try:

            status, data = self.mail.fetch(email_id, "(RFC822)")

            if status != "OK":

                raise EmailFetchError(
                    f"Unable to fetch email {email_id}."
                )

            logger.info(f"Fetched email {email_id}.")

            return data[0][1]

        except Exception as e:

            logger.error(f"Email fetch failed: {e}")

            raise EmailFetchError(
                "Unable to fetch email."
            )