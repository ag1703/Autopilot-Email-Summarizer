from email_service.imap_client import GmailClient
from email_service.parser import parse_email


def main():

    client = GmailClient()

    client.connect()

    client.open_inbox()

    ids = client.search_unread()

    if not ids:

        print("No unread emails.")

        client.disconnect()

        return

    latest = ids[-1]

    raw_email = client.fetch_email(latest)

    parsed = parse_email(raw_email)

    print()

    print("=" * 60)

    print("FROM")

    print(parsed["from"])

    print()

    print("SUBJECT")

    print(parsed["subject"])

    print()

    print("DATE")

    print(parsed["date"])

    print()

    print("BODY")

    print(parsed["body"][:1000])

    print("=" * 60)

    client.disconnect()


if __name__ == "__main__":

    main()