"""Manages setting the plant species, as the needed amount
of water differs based on the plant."""
from flask import (
    Blueprint, request, jsonify
)

from http_routes.auth import login_required
from db import get_db
import time

bp = Blueprint('characteristics', __name__, url_prefix='/characteristics')


@bp.route('/set', methods=["POST"])
@login_required
def set():
    """
    Sets the characteristics of the plant.
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - ideal_humidity
            - ideal_temperature
          properties:
            ideal_humidity:
              type: number
              description: the ideal humidity for the plant
            ideal_temperature:
              type: number
              description: the ideal temperature for the plant
    responses:
      200:
        description: everything went fine.
      403:
        description: user is not authenticated.
      422:
        description: required parameters not supplied.
    """
    request_data = request.get_json()

    if request_data is None or 'ideal_humidity' not in request_data:
        return jsonify({'message': 'Ideal humidity value is required.'}), 422

    ideal_humidity = request_data['ideal_humidity']

    try:
        float(ideal_humidity)
    except:
        return jsonify({'message': 'Ideal humidity must be numeric.'}), 422

    if request_data is None or 'ideal_temperature' not in request_data:
        return jsonify(
            {'message': 'Ideal temperature value is required.'}), 422

    ideal_temperature = request_data['ideal_temperature']

    try:
        float(ideal_temperature)
    except:
        return jsonify({'message': 'Ideal temperature must be numeric.'}), 422

    db = get_db()
    db.execute(
        'INSERT INTO characteristics (timestamp, ideal_humidity, ideal_temperature)'
        ' VALUES (?, ?, ?) ', (time.time(), ideal_humidity, ideal_temperature))
    db.commit()

    return jsonify({'message': 'Successfully set characteristics.'}), 200
