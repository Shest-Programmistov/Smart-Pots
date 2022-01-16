"""Endpoint returning plot showing the watering history."""
from datetime import datetime
from db import get_db
import time
from flask import (
    Blueprint
)

bp = Blueprint('plot_api', __name__, url_prefix='/plot')

@bp.route('/')
def plot():
    # current_date = datetime.fromtimestamp(time.time())

    data = get_db().execute(
        'SELECT timestamp, value'
        ' FROM water'
    ).fetchall()

    timestamps = [x[0] for x in data]
    values = [x[1] for x in data]

    

    return "SUCCESS", 200

# print("current_date =", current_date)
# print("type(current_date) =", type(current_date))

