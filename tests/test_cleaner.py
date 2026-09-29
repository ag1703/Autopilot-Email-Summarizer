from email_service.cleaner import clean_email


sample_html = """
<html>
<body>

<h1>Meeting Reminder</h1>

<p>Hello Arnav,</p>

<p>Your meeting starts at <b>10 AM</b>.</p>

<p>Regards,<br>Team</p>

</body>
</html>
"""

print(clean_email(sample_html))