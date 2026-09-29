from slack_service.formatter import format_summary


def main():

    email_data = {
        "subject": "Weekly Team Meeting",
        "from": "manager@company.com",
        "date": "18 July 2026",
        "body": "This is a sample email."
    }

    summary = """
• Meeting tomorrow

• Bring presentation

• Starts at 10 AM
"""

    message = format_summary(
        email_data,
        summary
    )

    print(message)


if __name__ == "__main__":

    main()