from email_service.imap_client import GmailClient
from email_service.parser import parse_email
from llm_service.summarizer import summarize_email
from llm_service.summary_writer import save_summary


def main():

    client = GmailClient()

    try:

        client.connect()

        client.open_inbox()

        ids = client.search_unread()

        if not ids:

            print("No unread emails found.")

            return

        latest = ids[-1]

        raw_email = client.fetch_email(latest)

        parsed = parse_email(raw_email)

        summary = summarize_email(parsed)

        file_path = save_summary(parsed, summary)

        print()

        print("=" * 60)

        print(summary)

        print("=" * 60)

        print()

        print(f"Saved to: {file_path}")

    except Exception as e:

        print()

        print("Pipeline failed.")

        print(e)

    finally:

        try:
            client.disconnect()
        except:
            pass

if __name__ == "__main__":
    main()