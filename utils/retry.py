import time

from utils.logger import logger


def retry_with_backoff(
    function,
    max_attempts=3,
    delay=2,
    operation_name="Operation"
):
    """
    Executes a function and retries it if it fails.

    Parameters:
        function:
            The function to execute.

        max_attempts:
            Maximum number of total attempts.

        delay:
            Number of seconds between attempts.

        operation_name:
            Human-readable name used in logs.
    """

    for attempt in range(1, max_attempts + 1):

        try:

            logger.info(
                f"{operation_name}: attempt "
                f"{attempt}/{max_attempts}"
            )

            return function()

        except Exception as e:

            logger.error(
                f"{operation_name} failed on attempt "
                f"{attempt}/{max_attempts}: {e}"
            )

            if attempt == max_attempts:

                logger.error(
                    f"{operation_name} failed after "
                    f"{max_attempts} attempts."
                )

                raise

            logger.info(
                f"Retrying {operation_name} "
                f"in {delay} seconds..."
            )

            time.sleep(delay)