"""Humidity endpoint"""
from flask import (
    Blueprint, request, jsonify
)

from db import get_db
import time

bp = Blueprint('humidity', __name__, url_prefix='/humidity')


@bp.route('/set', methods=["POST"])
def set():
    """
    Sets the humidity level.
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - value
          properties:
            value:
              type: number
              description: the humidity level
    responses:
      200:
        description: everything went fine.
      403:
        description: value not supplied.
    """
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
