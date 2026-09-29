from pathlib import Path
from datetime import datetime

from utils.logger import logger


SUMMARY_FOLDER = Path("summaries")


def save_summary(email_data, summary):
    """
    Saves the generated summary to a text file.
    """

    SUMMARY_FOLDER.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = SUMMARY_FOLDER / f"summary_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("EMAIL SUMMARY\n")
        file.write("=" * 60)
        file.write("\n\n")

        file.write(f"Subject: {email_data['subject']}\n")
        file.write(f"From: {email_data['from']}\n")
        file.write(f"Date: {email_data['date']}\n\n")

        file.write("SUMMARY\n")
        file.write("-" * 60)
        file.write("\n")

        file.write(summary)

    logger.info(f"Summary saved to {filename}")

    return filename