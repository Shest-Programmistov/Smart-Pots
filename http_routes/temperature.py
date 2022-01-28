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
    """
    Sets the temperature level.
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - degrees
          properties:
            degrees:
              type: number
              description: the number of degrees to set to
    responses:
      200:
        description: everything went fine.
      422:
        description: degrees not supplied.
    """

    if not 'degrees' in request.form:
        return jsonify({'message': 'Degrees are required.'}), 422

    degrees = request.form['degrees']

    try:
        float(degrees)
    except:
        return jsonify({'message': 'Degrees must be numeric.'}), 422

    db = get_db()
    db.execute(
        'INSERT INTO temperature (timestamp, value)'
        ' VALUES (?, ?) ',
        (time.time(), degrees)
    )
    db.commit()

    return jsonify({'message': 'Successfully recorded temperature value.'}), 200
