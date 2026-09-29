from pipeline import run_pipeline

from utils.logger import logger


def ai_job():
    """
    Runs the complete AutoPilot email processing pipeline.
    """

    logger.info("Scheduled AutoPilot pipeline started.")

    print("=" * 60)
    print("Running Scheduled AutoPilot Pipeline")
    print("=" * 60)

    try:

        run_pipeline()

        logger.info(
            "Scheduled AutoPilot pipeline completed successfully."
        )

        print("=" * 60)
        print("Scheduled AutoPilot Pipeline Completed")
        print("=" * 60)

    except Exception as e:

        logger.error(
            f"Scheduled AutoPilot pipeline failed: {e}"
        )

        print("=" * 60)
        print("Scheduled AutoPilot Pipeline Failed")
        print(e)
        print("=" * 60)

        raise