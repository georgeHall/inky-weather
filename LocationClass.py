import requests
import inspect
import json

import logging 
logger = logging.getLogger(__name__)


class Location():
    
    def __init__(self):
        self.__headers = {}
        self.__params = {}

    def get_location(self, address):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        lat = 51.4585656
        long = -0.2068795
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
        return (lat, long)