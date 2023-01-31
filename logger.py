import logging
import os
from pathlib import Path

HERE = Path(__file__).parent

LOG_FILE = HERE / "logger.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def log_exception(e) -> None:
    logging.exception(e)


def log_error(error) -> None:
    logging.error(error)


def log_info(info) -> None:
    logging.info(info)
