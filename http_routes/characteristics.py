"""Manages setting the plant species, as the needed amount
of water differs based on the plant."""
from flask import (
    Blueprint, request, jsonify
)
from db import get_db
import time

bp = Blueprint('characteristics', __name__, url_prefix='/characteristics')


@bp.route('/set', methods=["POST"])
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
      422:
        description: required parameters not supplied.
    """
    if not 'ideal_humidity' in request.form:
      return jsonify({'message': 'Ideal humidity value is required.'}), 422
    
    ideal_humidity = request.form['ideal_humidity']

    if not ideal_humidity.isnumeric():
      return jsonify({'message': 'Ideal humidity value must be numeric.'}), 422

    if not 'ideal_temperature' in request.form:
        return jsonify({'message': 'Ideal temperature value is required.'}), 422

    ideal_temperature = request.form['ideal_temperature']
    
    if not ideal_temperature.isnumeric():
      return jsonify({'message': 'Ideal temperature value must be numeric.'}), 422

    db = get_db()
    db.execute(
        'INSERT INTO characteristics (timestamp, ideal_humidity, ideal_temperature)'
        ' VALUES (?, ?, ?) ',
        (time.time(), ideal_humidity, ideal_temperature)
    )
    db.commit()

    return jsonify({'message': 'Successfully set characteristics.'}), 200