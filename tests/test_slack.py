from slack_service.slack_client import post_to_slack
from slack_service.formatter import format_summary


def main():

    email_data = {
        "subject": "Slack Integration Test",
        "from": "autopilot@example.com",
        "date": "18 July 2026",
        "body": ""
    }

    summary = """
• Slack connection successful.

• Formatter working correctly.

• Ready for pipeline integration.
"""

    message = format_summary(
        email_data,
        summary
    )

    post_to_slack(message)


if __name__ == "__main__":

    main()