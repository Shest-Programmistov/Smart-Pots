from math import degrees
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from db import get_db
import time

bp = Blueprint('temperature', __name__, url_prefix='/temperature')

@bp.route('/set', methods=["POST"])
def set():
    degrees = request.form['degrees']

    db = get_db()
    db.execute(
        'INSERT INTO temperature (timestamp, value)'
        ' VALUES (?, ?) ',
        (time.time(), degrees)
    )
    db.commit()

    return 'SUCCESS', 200
