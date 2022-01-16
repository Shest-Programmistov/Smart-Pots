"""Temperature endpoint"""
from math import degrees
from flask import (
    Blueprint, request, jsonify
)

from db import get_db
import time

bp = Blueprint('temperature', __name__, url_prefix='/temperature')


@bp.route('/set', methods=["POST"])
def set():
    """Sets the temperature level."""
    degrees = request.form['degrees']

    db = get_db()
    db.execute(
        'INSERT INTO temperature (timestamp, value)'
        ' VALUES (?, ?) ',
        (time.time(), degrees)
    )
    db.commit()

    return "SUCCESS", 200
    # check = get_db().execute(
    #     'SELECT id, timestamp, value'
    #     ' FROM temperature'
    #     ' ORDER BY timestamp DESC'
    # ).fetchone()
    # return jsonify({
    #     'status': 'Temperature level succesfully recorded',
    #     'data': {
    #         'id': check['id'],
    #         'timestamp': check['timestamp'],
    #         'value': check['value']
    #     }
    # }), 200
