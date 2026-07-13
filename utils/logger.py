import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/autopilot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("AutoPilot")