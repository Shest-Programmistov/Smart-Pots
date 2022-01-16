"""Humidity endpoint"""
from flask import (
    Blueprint, request, jsonify
)

from db import get_db
import time

bp = Blueprint('humidity', __name__, url_prefix='/humidity')


@bp.route('/set', methods=["POST"])
def set():
    """Sets the humidity level."""
    value = request.form['value']

    if not value:
        return jsonify({'status': 'Value is required.'}), 403

    db = get_db()
    db.execute(
        'INSERT INTO humidity (timestamp, value)'
        ' VALUES (?, ?) ',
        (time.time(), value)
    )
    db.commit()


    return "SUCCESS", 200
    # check = get_db().execute(
    #     'SELECT id, timestamp, value'
    #     ' FROM humidity'
    #     ' ORDER BY timestamp DESC'
    # ).fetchone()
    # return jsonify({
    #     'status': 'Humidity level succesfully recorded',
    #     'data': {
    #         'id': check['id'],
    #         'timestamp': check['timestamp'],
    #         'value': check['value']
    #     }
    # }), 200
