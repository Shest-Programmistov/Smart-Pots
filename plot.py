"""Endpoint returning plot showing the watering history."""
from datetime import datetime
from db import get_db
import time
from flask import (
    Blueprint
)
import pylab as pl
import numpy as np
import pandas as pd


bp = Blueprint('plot_api', __name__, url_prefix='/plot')


def generate_plot(timestamps, values):
    N = 7 * 24 # 7 days, 24 hours
    np.random.seed(0)

    day = np.random.randint(0, 7, N*2)
    hour = np.random.randint(0, 24, N)
    water_qty = np.random.randint(0, 200, N)

    df = pd.DataFrame({"day": day, "hour": hour, "water_qty": water_qty})
    df.drop_duplicates(subset=["day", "hour"], inplace=True)

    df2 = df.pivot(columns="hour", index="day", values="water_qty")
    df2.fillna(0, inplace=True)

    day, hour = np.mgrid[:df2.shape[0]+1, :df2.shape[1]+1]
    fig, ax = pl.subplots(figsize=(12, 4))
    ax.set_aspect("equal")
    pl.pcolormesh(hour, day, df2.values, cmap="Greens", edgecolor="w", vmin=-10, vmax=100)
    pl.xlim(0, df2.shape[1])
    fig.savefig('a.jpg')



@bp.route('/')
def plot():
    data = get_db().execute(
        'SELECT timestamp, value'
        ' FROM water'
    ).fetchall()

    timestamps = [x[0] for x in data]
    values = [x[1] for x in data]

    generate_plot(timestamps, values)

    return "SUCCESS", 200