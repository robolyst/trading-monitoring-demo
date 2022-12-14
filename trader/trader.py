from time import sleep
import numpy as np
import structlog
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
file_handler = logging.FileHandler('/var/log/trader/trader.logs')
logger.addHandler(file_handler)

structlog.configure_once(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer(),
    ],
)

json_logger = structlog.wrap_logger(logger)

price = 100

json_logger.info(event="startup")

while True:
    sleep(0.5)

    price = price * (1 + np.random.randn() * 0.01)
    json_logger.info(event="price", price=price)