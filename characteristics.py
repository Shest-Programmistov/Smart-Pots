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
    Sets the hcharacteristics of the plant.
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
              type: float
              description: the ideal humidity for the plant
            ideal_temperature:
              type: float
              description: the ideal temperature for the plant
    responses:
      200:
        description: everything went fine.
      403:
        description: required parameters not supplied.
    """
    ideal_humidity = request.form['ideal_humidity']
    ideal_temperature = request.form['ideal_temperature']

    if not ideal_humidity:
        return jsonify({'status': 'Ideal humidity value is required.'}), 403

    if not ideal_temperature:
        return jsonify({'status': 'Ideal temperature value is required.'}), 403

    db = get_db()
    db.execute(
        'INSERT INTO characteristics (timestamp, ideal_humidity, ideal_temperature)'
        ' VALUES (?, ?, ?) ',
        (time.time(), ideal_humidity, ideal_temperature)
    )
    db.commit()


    return "SUCCESS", 200