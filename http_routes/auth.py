import functools

from flask import (Blueprint, g, request, session, jsonify)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=["POST"])
def register():
    """
    Registers a new user.
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: the login name for the new user
            password:
              type: string
              description: the password for the new user
    responses:
      200:
        description: user registered succesfully.
      403:
        description: there is already an user with that username
      422:
        description: required parameters not supplied.
    """

    request_data = request.get_json()

    if request_data is None or 'username' not in request_data:
        return jsonify({'status': 'Username is required.'}), 422
    elif 'password' not in request_data:
        return jsonify({'status': 'Password is required.'}), 422

    username = request_data['username']
    password = request_data['password']

    db = get_db()

    try:
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db.commit()
    except db.IntegrityError:
        return jsonify(
            {'status': f'User {username} is already registered.'}), 403

    return jsonify({'status': 'user registered succesfully'}), 200


@bp.route('/login', methods=["POST"])
def login():
    """
    Logs in a user.
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: the login name for the user
            password:
              type: string
              description: the password for the user
    responses:
      200:
        description: user logged in succesfully.
      403:
        description: there is no user with that username and password.
      422:
        description: required parameters not supplied.
    """

    request_data = request.get_json()

    if request_data is None or 'username' not in request_data:
        return jsonify({'status': 'Username is required.'}), 422
    elif request_data is None or 'password' not in request_data:
        return jsonify({'status': 'Password is required.'}), 422

    username = request_data['username']
    password = request_data['password']
    db = get_db()

    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        return jsonify({'status': 'username not found'}), 403
    elif not check_password_hash(user['password'], password):
        return jsonify({'status': 'password is incorrect'}), 403

    session.clear()
    session['user_id'] = user['id']
    return jsonify({'status': 'user logged in succesfully'}), 200


@bp.route('/logout')
def logout():
    """
    Logs out the current user.
    ---
    responses:
      200:
        description: user logged out succesfully.
      403:
        description: user is not authenticated.
    """
    session.clear()
    return jsonify({'status': 'user logged out succesfully'}), 200


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return jsonify({'status': 'User is not authenticated'}), 403

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
