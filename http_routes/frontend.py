from flask import Blueprint, render_template, session
from http_routes.auth import login_required

bp = Blueprint('frontend', __name__)


@bp.route('/')
def index():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/home')
@login_required
def home():
    return render_template('home.html')
