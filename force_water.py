# Aici o sa facem un endpoint care, atunci cand e apelat, uda planta cu ceva parametru (pentru user).

from math import degrees
from water_util import water_plant
from flask import (
    Blueprint, request
)

from db import get_db
import time

bp = Blueprint('force_water', __name__, url_prefix='/force_water')

@bp.route('/', methods=["POST"])
def set():
    value = request.form['value']
    water_plant(value)

    return 'SUCCESS', 200