import email
from email import policy
from bs4 import BeautifulSoup

from utils.logger import logger


def parse_email(raw_email):
    """
    Parses raw email bytes and extracts useful information.
    """

    try:

        message = email.message_from_bytes(
            raw_email,
            policy=policy.default
        )

        email_data = {
            "from": message.get("From"),
            "to": message.get("To"),
            "subject": message.get("Subject"),
            "date": message.get("Date"),
            "body": extract_body(message)
        }

        logger.info(
            f"Email cleaned and parsed: {email_data['subject']}"
        )

        return email_data

    except Exception as e:

        logger.error(f"Email parsing failed: {e}")
        raise



def extract_body(message):
    """
    Extracts the email body.
    Prefers HTML if available because newsletters
    are usually much better formatted in HTML.
    """

    html_body = None
    plain_body = None

    if message.is_multipart():

        for part in message.walk():

            content_type = part.get_content_type()
            disposition = str(part.get("Content-Disposition"))

            if "attachment" in disposition:
                continue

            if content_type == "text/plain" and plain_body is None:
                plain_body = part.get_content()

            elif content_type == "text/html" and html_body is None:
                html_body = part.get_content()

    else:

        if message.get_content_type() == "text/html":
            html_body = message.get_content()
        else:
            plain_body = message.get_content()

    if html_body:
        soup = BeautifulSoup(html_body, "html.parser")
        return soup.get_text(separator="\n")

    return plain_body or ""