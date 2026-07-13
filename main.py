import time

from scheduler.scheduler import start_scheduler


def main():

    start_scheduler()

    print("AutoPilot Running...")

    try:

        while True:

            time.sleep(2)

    except KeyboardInterrupt:

        print("\nStopping...")


if __name__ == "__main__":
    main()