#!/usr/bin/env python3
import sys
import logging
import signal

from inky.auto import auto
import RPi.GPIO as GPIO
from clear import clear

from OpenWeatherClass import OpenWeather
from LocationClass import Location
from ConfigClass import Config
from DisplayClass import Display

logging.basicConfig(level=logging.DEBUG, filename="weather.log", format="%(asctime)s %(levelname)s:%(message)s")
logger = logging.getLogger(__name__)


BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'C', 'D']

inky = auto(ask_user=True, verbose=True)

config = Config()
weather = OpenWeather(api_key=config.get_open_weather_api_token())
location = Location()
display = Display(inky=inky)

def button_A():
    print("A")
    
def button_B():
    address = config.get_address()
    lat, long = location.get_location(address=address)
    weather.get_weather_5day_3hour(lat=lat,long=long)
    
def button_C():   
    address = config.get_address()
    lat, long = location.get_location(address=address)
    weather_json = weather.get_weather_5day_3hour(lat=lat,long=long)
    weather_list = weather_json["list"]
    weather_list_daily = []
    for x in weather_list[:6]:
        weather_list_daily.append(x)
    
    display.display(weather=weather_list_daily)
    
def button_D():
    clear(inky=inky)

# "handle_button" will be called every time a button is pressed
# It receives one argument: the associated input pin.
def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    logger.info(f"Button {pin = }, {label = }")

    if label == "A":
        button_A()

    if label == "B":
        button_B()

    if label == "C":
        button_C()

    if label == "D":
        button_D()
    
def init_buttons():
    logger.info("START: init_buttons()")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    for pin in BUTTONS:
        GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=250)
    logger.info("END: init_buttons()")

def main():
    init_buttons()
    logger.info("signal.pause()")
    signal.pause()

if __name__ == '__main__':
    main()
