from math import degrees
from flask import (
    Blueprint, request
)

from db import get_db
import time

bp = Blueprint('humidity', __name__, url_prefix='/humidity')

@bp.route('/set', methods=["POST"])
def set():
    value = request.form['value']

    db = get_db()
    db.execute(
        'INSERT INTO humidity (timestamp, value)'
        ' VALUES (?, ?) ',
        (time.time(), value)
    )
    db.commit()

    return 'SUCCESS', 200
