"""Endpoint force_water - when called, proceeds to water the plant
with a specified value/ amount of water."""

from water_util import water_plant
from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('force_water', __name__, url_prefix='/force_water')


@bp.route('/', methods=["POST"])
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
        description: value not supplied.
    """
    value = request.form['value']
    if not value:
        return jsonify({'status': 'Value is required.'}), 403

    water_plant(value)

    return 'SUCCESS', 200
