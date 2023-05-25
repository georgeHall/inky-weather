import inspect
import logging 

import yaml
from yaml.loader import SafeLoader

logger = logging.getLogger(__name__)

class Config():
    
    def __init__(self):
        with open("config.yaml", "r") as f:
            self.__full_config = list(yaml.load_all(f, Loader=SafeLoader))
            self.__open_weather_api_key = self.__full_config[0]["weather"]["api_key"]
            self.__address = self.__full_config[0]["weather"]["api_key"]
            
    def get_open_weather_api_token(self):
        return self.__open_weather_api_key
    
    def get_address(self):
        return self.__address