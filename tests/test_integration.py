import sqlite3
import pytest
import tempfile
import os, sys
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from app import create_app
import db
import water
import water_util


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(testing=True, db_path=db_path)

    with app.app_context():
        db.close_db()
        db.init_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.mark.integtest
def test_app(app, client):
    with app.app_context():
        # Register
        response = client.post('/auth/register', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200

        # Login
        response = client.post('auth/login', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200

        # Set plant characteristics
        response = client.post('/characteristics/set', data={'ideal_humidity': 70, 'ideal_temperature': 10}, follow_redirects=True)
        assert response.status_code == 200

        # Set temperature
        response = client.post('/temperature/set', data={'degrees': 22.37}, follow_redirects=True)
        assert response.status_code == 200

        # Set humidity
        response = client.post('/humidity/set', data={'value': 41.927}, follow_redirects=True)
        assert response.status_code == 200

        # Water status => should tell us to water
        response = water.get_status()
        assert response['status'] == 'success' and response['data']['water'] == 1

        # Water plant
        timestamp = time.time()
        qty = response['data']['qty']
        water_util.water_plant(qty, timestamp)
        entry = db.get_db().execute(
            'SELECT value'
            ' FROM water'
            f' WHERE timestamp = {str(timestamp)} and value = {str(qty)}' 
        ).fetchone()
        assert(entry is not None)

        # Set plant characteristics
        response = client.post('/characteristics/set', data={'ideal_humidity': 10, 'ideal_temperature': 10}, follow_redirects=True)
        assert response.status_code == 200

        # Set humidity
        response = client.post('/humidity/set', data={'value': 20}, follow_redirects=True)
        assert response.status_code == 200

        # Force water
        response = client.post('/force_water', data={'value': 100}, follow_redirects=True)
        assert response.status_code == 200

        # Water status => should tell us not to water
        response = water.get_status()
        assert response['status'] == 'success' and response['data']['water'] == 0

        # Logout
        response = client.get('/auth/logout', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200