"""Water logic"""
from db import get_db

def get_status():
    # temperature = get_db().execute(
    #     'SELECT id, timestamp, value'
    #     ' FROM temperature'
    #     ' ORDER BY timestamp DESC'
    # ).fetchone()
    temperature = get_db().execute(
        'SELECT id, value'
        ' FROM temperature'
        ' ORDER BY id DESC'
    ).fetchone()

    # humidity = get_db().execute(
    #     'SELECT id, timestamp, value'
    #     ' FROM humidity'
    #     ' ORDER BY timestamp DESC'
    # ).fetchone()
    humidity = get_db().execute(
        'SELECT id, value'
        ' FROM humidity'
        ' ORDER BY id DESC'
    ).fetchone()


    if temperature is None:
        return {'status': 'Please set a value for temperature'}

    if humidity is None:
        return {'status': 'Please set a value for humidity'}

    return {
        'data': {
            'watered': "merge:)"
        }
    }
