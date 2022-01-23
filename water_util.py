"""Utils for water functionality"""
from db import get_db


def water_plant(water, timestamp):
    db = get_db()
    db.execute(
        'INSERT INTO water (timestamp, value)'
        ' VALUES (?, ?) ',
        (timestamp, water)
    )
    db.commit()
