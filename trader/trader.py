from time import sleep
import numpy as np
import structlog
import logging
import os

LOG_FILE_NAME = os.environ['LOG_FILE_NAME']

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
file_handler = logging.FileHandler(LOG_FILE_NAME)
logger.addHandler(file_handler)

# Configure the structured logger
structlog.configure_once(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer(),
    ],
)

# Wrap the root logger with the structured logger
json_logger = structlog.wrap_logger(logger)

price = 100

while True:
    price = price * (1 + np.random.randn() * 0.01)

    # Log price in JSON
    json_logger.info(event="price_log", price=price)

    sleep(0.5)