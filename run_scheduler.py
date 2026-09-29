import time

from scheduler.scheduler import start_scheduler


def main():

    start_scheduler()

    print("Scheduler is running. Press Ctrl+C to stop.")

    try:

        while True:

            time.sleep(60)

    except KeyboardInterrupt:

        print("\nScheduler stopped.")


if __name__ == "__main__":

    main()