"""Endpoint force_water - when called, proceeds to water the plant
with a specified value/ amount of water."""

from water_util import water_plant
from flask import (
    Blueprint, request, jsonify
)
from http_routes.auth import login_required
import time

bp = Blueprint('force_water', __name__)


@bp.route('/force_water', methods=["POST"])
@login_required
def force_water():
    """
    Waters the plant immediately.
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
              description: the quantity of water
    responses:
      200:
        description: everything went fine.
      403:
        description: user is not authenticated.
      422:
        description: value not supplied.
    """

    if not 'value' in request.form:
      return jsonify({'message': 'Value is required.'}), 422

    value = request.form['value']

    if not value.isnumeric():
      return jsonify({'message': 'Value must be numeric.'}), 422

    water_plant(value, time.time())

    return jsonify({'message': 'Successfully watered plant.'}), 200
