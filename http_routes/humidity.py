"""Humidity endpoint"""
import re
from flask import (
    Blueprint, request, jsonify
)

from http_routes.auth import login_required
from db import get_db
import time

bp = Blueprint('humidity', __name__, url_prefix='/humidity')


@bp.route('/set', methods=["POST"])
@login_required
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
        description: user is not authenticated.
      422:
        description: value not supplied.
    """

    request_data = request.get_json()

    if request_data is None or not 'value' in request_data:
        return jsonify({'message': 'Value is required.'}), 422

    value = request_data['value']

    try:
        float(value)
    except:
        return jsonify({'message': 'Value must be numeric.'}), 422

    db = get_db()
    db.execute(
        'INSERT INTO humidity (timestamp, value)'
        ' VALUES (?, ?) ',
        (time.time(), value)
    )
    db.commit()

    return jsonify({'message': 'Successfully recorded humidity value.'}), 200
