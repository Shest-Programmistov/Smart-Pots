"""Endpoint force_water - when called, proceeds to water the plant
with a specified value/ amount of water."""

from water_util import water_plant
from flask import (
    Blueprint, request
)

bp = Blueprint('force_water', __name__, url_prefix='/force_water')


@bp.route('/', methods=["POST"])
def set():
    value = request.form['value']
    water_plant(value)

    return 'SUCCESS', 200
