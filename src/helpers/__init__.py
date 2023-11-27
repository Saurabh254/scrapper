import logging
from ._logger import CustomFormatter
from .db import cur, conn
from .mics import generateProductId


# create logger with 'logging.py'
logger = logging.getLogger("My_app")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)


__all__ = [
    logger,
    cur,
    conn
]
