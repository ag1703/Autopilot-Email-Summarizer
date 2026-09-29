def format_summary(email_data, summary):
    """
    Formats an email summary into a Slack message.
    """

    message = f"""
📧 *New Email Summary*

*Subject:*
{email_data["subject"]}

*From:*
{email_data["from"]}

*Date:*
{email_data["date"]}

*Summary:*
{summary}
"""

    return message.strip()