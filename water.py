"""Water logic"""
from db import get_db
from water_util import water_plant


def get_water_qty(temperature, humidity, coef = 0.5, x = 3, y = 5):
    return (temperature * x + humidity * y ) * coef


def get_status():
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
        return {'status': 'Please set a value for temperature'}

    if humidity is None:
        return {'status': 'Please set a value for humidity'}

    temperature, humidity = temperature[0], humidity[0]
    water_qty = get_water_qty(temperature, humidity)
    if water_qty:
        water_plant(water_qty)    

    return {
        'data': {
            'water': water_qty != 0,
            'qty': water_qty    
        }
    }
