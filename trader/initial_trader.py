from time import sleep
import numpy as np
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
file_handler = logging.FileHandler('/var/log/trader/trader.logs')
logger.addHandler(file_handler)

price = 100

logger.info("startup")

while True:
    sleep(0.5)

    price = price * (1 + np.random.randn() * 0.01)
    logger.info(f"price {price}")