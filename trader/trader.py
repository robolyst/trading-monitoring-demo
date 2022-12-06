from time import sleep
import numpy as np
import structlog
import logging


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs.json')
root_logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
root_logger.addHandler(console_handler)

structlog.configure_once(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.JSONRenderer(),
    ],
)

logger = structlog.wrap_logger(root_logger)

price = 100

while True:
    sleep(0.1)

    price = price * (1 + np.random.randn() * 0.01)
    logger.info(event="price", price=price)