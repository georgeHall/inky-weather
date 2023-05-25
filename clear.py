import argparse
import time

from inky.auto import auto
from PIL import Image
import logging 

from inky.inky_uc8159 import CLEAN
logger = logging.getLogger(__name__)


def clear(inky):
    logger.info("START: clear")
    for _ in range(2):
        for y in range(inky.height - 1):
            for x in range(inky.width - 1):
                inky.set_pixel(x, y, CLEAN)

        inky.show()
        time.sleep(1.0)
        
    logger.info("END: clear")