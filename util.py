import inspect
import logging
from Enums import Temperature

logger = logging.getLogger(__name__)
    
def temperature_conversion(kelvin):
    logger.debug(f"START: {inspect.currentframe().f_code.co_name}")
    farenheight = (9 * (kelvin - 273)) / 5 + 32
    celcius = kelvin - 273.15
    logger.debug(f"END: {inspect.currentframe().f_code.co_name}")
    return {Temperature.KELVIN: kelvin, Temperature.FARENHEIGHT: farenheight, Temperature.CELCIUS: celcius}