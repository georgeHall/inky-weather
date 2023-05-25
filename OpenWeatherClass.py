import requests
import json
import inspect
import shutil
import os

from Enums import Temperature

import logging
logger = logging.getLogger(__name__)

# inspect.currentframe().f_code.co_name


class OpenWeather():

    def __init__(self, api_key):
        self.__headers = {}
        self.__params = {}
        self.__api_key = api_key
        self.__url = "https://api.openweathermap.org/data/2.5/forecast"
        self.__symbol_url = "http://openweathermap.org/img/wn"
        self.__symbol_dir = "./symbols"

        self.load_symbols()

    def get_weather_5day_3hour(self, lat, long):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        url = f"{self.__url}?lat={lat}&lon={long}&appid={self.__api_key}"
        response = self.__get(url=url)
        # print(f"{response = }")
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
        return response


    def get_symbol(self, icon):
        return f"{self.__symbol_dir}/{icon}.png"
    
    def __get(self, url):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        response = requests.get(
            url=url, headers=self.__headers, params=self.__params)
        response_json = json.loads(response.text)
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
        return response_json

    def load_symbols(self):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        if not os.path.exists(self.__symbol_dir):
            os.makedirs(self.__symbol_dir)

        for symbol in ["01d", "02d", "03d", "04d", "09d", "10d", "11d", "13d", "50d",
                       "01n", "02n", "03n", "04n", "09n", "10n", "11n", "13n", "50n"]:
            if os.path.exists(f"{self.__symbol_dir}/{symbol}.png"):
                continue
            response = requests.get(
                url=f"{self.__symbol_url}/{symbol}@2x.png", stream=True)
            if response.status_code == 200:
                with open(f"./symbols/{symbol}.png", 'wb') as file:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, file)
        
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
