import logging
import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def console_logger(name: str, level: LogLevel) -> logging.Logger:

    logger = logging.getLogger(f"__{name}__")
    logger.setLevel(level.value)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level.value)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S%p",
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


def file_logger(name: str, level: LogLevel) -> logging.Logger:
    
    logger = logging.getLogger(f"__{name}__")
    logger.setLevel(level.value)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_handler = logging.FileHandler(f"logs/{name}_run.log")
    file_handler.setLevel(level.value)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S%p",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger