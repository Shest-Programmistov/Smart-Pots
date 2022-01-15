from math import degrees
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from db import get_db

bp = Blueprint('temperature', __name__, url_prefix='/temperature')

@bp.route('/set', methods=["POST"])
def set():
    degrees = request.form['degrees']
    # Mergem in baza de date si salvam timestamp-ul curent si degrees
