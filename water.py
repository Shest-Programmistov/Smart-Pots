"""Water logic"""
from db import get_db
from water_util import water_plant
import time


def get_water_qty(temperature, humidity, coef = 0.5, x = 3, y = 5):
    return (temperature * x + humidity * y ) * coef


def get_status():
    """Returns how much water to send through the water 
    pump at a specific time interval."""
    temperature = get_db().execute(
        'SELECT value'
        ' FROM temperature'
        ' ORDER BY timestamp DESC'
    ).fetchone()

    humidity = get_db().execute(
        'SELECT value'
        ' FROM humidity'
        ' ORDER BY timestamp DESC'
    ).fetchone()

    if temperature is None:
        return {
            'status': 'fail',
            'message': 'Please set a value for temperature'
        }

    if humidity is None:
        return {
            'status': 'fail',
            'message': 'Please set a value for humidity'
        }

    temperature, humidity = temperature[0], humidity[0]
    water_qty = get_water_qty(temperature, humidity)
    if water_qty:
        water_plant(water_qty, time.time())    

    return {
        'status': 'success',
        'data': {
            'water': water_qty != 0,
            'qty': water_qty    
        }
    }
