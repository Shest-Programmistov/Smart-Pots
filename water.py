"""Water logic"""
from db import get_db
from water_util import water_plant
import time


def get_water_qty(temperature, humidity):
    ideals = get_db().execute(
        'SELECT ideal_temperature, ideal_humidity'
        ' FROM characteristics'
        ' ORDER BY timestamp DESC'
    ).fetchone()

    ideal_temperature, ideal_humidity = ideals
    ideal_temperature = float(ideal_temperature)
    ideal_humidity = float(ideal_humidity)

    # a normal plant needs around 100 milliliters of water per watering

    if humidity >= ideal_humidity: # it works
        return 0.0

    return ideal_temperature / temperature * (ideal_humidity - humidity) + 100

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
