from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from config.settings import DATABASE_URL
from scheduler.jobs import ai_job
from utils.logger import logger


scheduler = BackgroundScheduler(
    jobstores={
        "default": SQLAlchemyJobStore(
            url=DATABASE_URL
        )
    }
)


def start_scheduler():
    """
    Starts the scheduler.
    """

    if not scheduler.running:

        scheduler.start()

        logger.info("Scheduler Started")

        print("Scheduler Started")

        if not scheduler.get_job("ai_job"):

            scheduler.add_job(
                ai_job,
                trigger="interval",
                minutes=1,
                id="ai_job",
                replace_existing=True
            )

            print("AI Job Scheduled")

            logger.info("AI Job Scheduled")