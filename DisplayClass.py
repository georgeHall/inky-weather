import os
import sys
import inspect
import logging
import time

from PIL import Image
from inky.auto import auto

from util import temperature_conversion

logger = logging.getLogger(__name__)

class Display:
    def __init__(self, inky):
        self.__inky = inky
        
    def load_image(self, image_path, saturation=0.5, rotate=-90):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        image = Image.open(image_path).rotate(rotate, expand=1)
        resized_image = image.resize(self.__inky.resolution)
        self.__inky.set_image(resized_image, saturation=saturation)
        # self.__inky.show()
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
       
    def __get_concat_v_cut(self, im1, im2):
        dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height + 2))
        dst.paste(im1, (0, 0))
        dst.paste(Image.new(mode="RGB", size=(400, 2), color=(50, 50, 50)), (0, im1.height))
        dst.paste(im2, (0, im1.height+2))
        return dst
     
     
    def __dt_txt_to_time(self, dt_txt):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        print(dt_txt)
        time = dt_txt.split(" ")[1]
        print(time)
        time = time[:-3]
        print(time)
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
        return ""
    
    def display(self, weather):
        logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
        
        path = "./images"
        if not os.path.exists(path):
            os.makedirs(path)
        
        img = Image.new(mode="RGB", size=(400, 0), color=(225, 225, 225))
        for index, value in enumerate(weather):
            print(self.__dt_txt_to_time(value["dt_txt"]))        
            new_img = Image.new(mode="RGB", size=(400, 105), color=(225, 225, 225))
            img = self.__get_concat_v_cut(img, new_img)
   
        result = "image.jpg"
        img.save(f"{path}/{result}")
        self.load_image(f"{path}/{result}", rotate=-90)
        logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
