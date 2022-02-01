"""Temperature endpoint"""
from flask import (
    Blueprint, request, jsonify
)

from db import get_db
import time
from http_routes.auth import login_required

bp = Blueprint('temperature', __name__, url_prefix='/temperature')


@bp.route('/set', methods=["POST"])
@login_required
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
      403:
        description: user is not authenticated.
      422:
        description: degrees not supplied.
    """

    request_data = request.get_json()

    if request_data is None or 'degrees' not in request_data:
        return jsonify({'message': 'Degrees are required.'}), 422

    degrees = request_data['degrees']

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

    return jsonify(
        {'message': 'Successfully recorded temperature value.'}), 200
