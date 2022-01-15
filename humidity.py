from math import degrees
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from db import get_db

bp = Blueprint('humidity', __name__, url_prefix='/humidity')

@bp.route('/set', methods=["POST"])
def set():
    value = request.form['value']
    # Mergem in baza de date si salvam timestamp-ul curent si value
