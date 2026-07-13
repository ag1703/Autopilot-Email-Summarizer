from email_service.imap_client import GmailClient


client = GmailClient()

client.connect()

print(client.mail)

client.disconnect()