
from math import degrees
from flask import (
    Blueprint, request
)

from db import get_db
import time


def water_plant(water):
	db = get_db()
	db.execute(
		'INSERT INTO water (timestamp, value)'
		' VALUES (?, ?) ',
		(time.time(), water)
	)
	db.commit()