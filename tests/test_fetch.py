from email_service.imap_client import GmailClient


def main():

    client = GmailClient()

    client.connect()

    client.open_inbox()

    ids = client.search_unread()

    if ids:

        latest = ids[-1]

        raw_email = client.fetch_email(latest)

        print(type(raw_email))

        print(f"Downloaded {len(raw_email)} bytes")

    else:

        print("No unread emails.")

    client.disconnect()


if __name__ == "__main__":

    main()