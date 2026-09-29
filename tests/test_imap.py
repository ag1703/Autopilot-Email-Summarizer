from email_service.imap_client import GmailClient


def main():

    client = GmailClient()

    client.connect()

    client.disconnect()


if __name__ == "__main__":

    main()