from datetime import datetime


from email_service.imap_client import GmailClient
from email_service.parser import parse_email


from llm_service.summarizer import summarize_email
from llm_service.summary_writer import save_summary


from slack_service.formatter import format_summary
from slack_service.slack_client import post_to_slack


from utils.logger import logger
from utils.retry import retry_with_backoff


def run_pipeline():
    """
    Runs the complete AutoPilot workflow.
    Processes every unread email in the inbox.
    """

    client = GmailClient()

    job_start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("AUTOPILOT JOB STARTED")
    logger.info(f"Start time: {job_start_time}")
    logger.info("=" * 60)

    try:

        logger.info("Starting AutoPilot pipeline.")

        client.connect()

        client.open_inbox()

        email_ids = client.search_unread()

        if not email_ids:

            print("No unread emails found.")

            logger.info("No unread emails found.")

            job_end_time = datetime.now()

            logger.info("=" * 60)
            logger.info("AUTOPILOT JOB COMPLETED")
            logger.info("Status: SUCCESS")
            logger.info("Emails processed: 0")
            logger.info(f"End time: {job_end_time}")
            logger.info("=" * 60)

            return

        print(f"Found {len(email_ids)} unread email(s).\n")

        logger.info(
            f"Processing {len(email_ids)} unread email(s)."
        )

        processed_count = 0

        for index, email_id in enumerate(email_ids, start=1):

            print("=" * 60)
            print(
                f"Processing Email "
                f"{index} of {len(email_ids)}"
            )
            print("=" * 60)

            logger.info(
                f"Processing email "
                f"{index} of {len(email_ids)}"
            )

            raw_email = retry_with_backoff(
                lambda: client.fetch_email(email_id),
                operation_name="Email fetch"
            )

            parsed_email = parse_email(raw_email)

            summary = summarize_email(parsed_email)

            logger.info(
                f"Summary preview: {summary[:200]}"
            )

            save_summary(
                parsed_email,
                summary
            )

            slack_message = format_summary(
                parsed_email,
                summary
            )

            post_to_slack(slack_message)

            processed_count += 1

            print(
                "Email processed successfully.\n"
            )

            logger.info(
                f"Email {index} processed successfully."
            )

        print("=" * 60)
        print(
            "Pipeline completed successfully."
        )
        print(
            f"Processed {processed_count} email(s)."
        )
        print("=" * 60)

        job_end_time = datetime.now()

        logger.info("=" * 60)
        logger.info("AUTOPILOT JOB COMPLETED")
        logger.info("Status: SUCCESS")
        logger.info(
            f"Emails processed: {processed_count}"
        )
        logger.info(
            f"End time: {job_end_time}"
        )
        logger.info("=" * 60)

    except Exception as e:

        job_end_time = datetime.now()

        logger.error("=" * 60)
        logger.error("AUTOPILOT JOB FAILED")
        logger.error("Status: FAILURE")
        logger.error(f"Error: {e}")
        logger.error(
            f"End time: {job_end_time}"
        )
        logger.error("=" * 60)

        print("\nPipeline failed.")

        print(e)

    finally:

        client.disconnect()