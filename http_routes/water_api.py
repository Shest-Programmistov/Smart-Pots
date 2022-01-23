"""sends how much water to send through the water 
pump at a specific time interval."""
from flask import (
    Blueprint
)

import water as water_status

bp = Blueprint('water_api', __name__)

@bp.route('/water')
def get_status_api():

    # TODO Right now default status code is 200, but the correct status code should be received
    # from bed_status.get_status().
    
    # call water_util.set to record the watering event?

    return water_status.get_status(), 200
