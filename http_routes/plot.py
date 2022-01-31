"""Endpoint returning plot showing the watering history."""
from datetime import datetime
from db import get_db
import time
from flask import (
    Blueprint,
    send_file
)
import pylab as pl
import numpy as np
import pandas as pd

import math
import time
from http_routes.auth import login_required
from datetime import datetime

bp = Blueprint('plot_api', __name__)


def generate_weekly_plot(timestamps, values, oneWeekAgo):
    day = [datetime.fromtimestamp(x - oneWeekAgo).day - 1 - 1 for x in timestamps]
    hour = [datetime.fromtimestamp(x).hour for x in timestamps]

    desiredShape = (7, 24)

    fig, ax = pl.subplots(figsize=(12, 4))
    ax.set_aspect("equal")

    dataset = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    datalen = len(values)

    for i in range(0, datalen):
        if day[i] >= 0 and day[i] <= 6:
            dataset[day[i]][hour[i]] += values[i]

    day, hour = np.mgrid[:desiredShape[0] + 1, :desiredShape[1] + 1]
    pl.pcolormesh(
        hour,
        day,
        dataset,
        cmap="Greens",
        edgecolor="w",
        vmin=-10,
        vmax=100)
    pl.xlim(0, desiredShape[1])
    fig.savefig('a.jpg')
    pl.close()


@bp.route('/plot')
@login_required
def plot():
    """
    Plots the water quantities over the last week divided by hours.
    ---
    responses:
      200:
        description: everything went fine.
      403:
        description: user is not authenticated.
    """

    nowTime = math.floor(time.time())
    oneWeek = 3600 * 24 * 7  # in seconds

    data = get_db().execute(
        'SELECT timestamp, value'
        ' FROM water WHERE timestamp >= ' + str(nowTime - oneWeek)
    ).fetchall()

    timestamps = [x[0] for x in data]
    values = [x[1] for x in data]

    generate_weekly_plot(timestamps, values, nowTime - oneWeek)

    return send_file("a.jpg", mimetype='image/jpg')


def generate_weekly_normal_graph(timestamps, values, oneWeekAgo):
    pl.plot(timestamps, values)
    pl.savefig('a.jpg')
    pl.close()


@bp.route('/plot_temperature')
@login_required
def plot_temperature():
    """
    Plots the temperature over the last week.
    ---
    responses:
      200:
        description: everything went fine.
      403:
        description: user is not authenticated.
    """

    nowTime = math.floor(time.time())
    oneWeek = 3600 * 24 * 7  # in seconds

    data = get_db().execute(
        'SELECT timestamp, value'
        ' FROM temperature WHERE timestamp >= ' + str(nowTime - oneWeek) + ' ORDER BY timestamp'
    ).fetchall()

    timestamps = [x[0] for x in data]
    values = [x[1] for x in data]

    generate_weekly_normal_graph(timestamps, values, nowTime - oneWeek)

    return send_file("a.jpg", mimetype='image/jpg'), 200


@bp.route('/plot_humidity')
@login_required
def plot_humidity():
    """
    Plots the humidity over the last week.
    ---
    responses:
      200:
        description: everything went fine.
      403:
        description: user is not authenticated.
    """

    nowTime = math.floor(time.time())
    oneWeek = 3600 * 24 * 7  # in seconds

    data = get_db().execute(
        'SELECT timestamp, value'
        ' FROM humidity WHERE timestamp >= ' + str(nowTime - oneWeek) + ' ORDER BY timestamp'
    ).fetchall()

    timestamps = [x[0] for x in data]
    values = [x[1] for x in data]

    generate_weekly_normal_graph(timestamps, values, nowTime - oneWeek)

    return send_file("a.jpg", mimetype='image/jpg'), 200
