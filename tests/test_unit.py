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


def authorize(client):
    client.post('/auth/register', json={'username': 'user', 'password': 'password'})
    client.post('auth/login', json={'username': 'user', 'password': 'password'})


# -------- DATABASE --------

def test_db_connection(app):
    with app.app_context():
        err = False
        try:
            entry = db.get_db().execute(
                'SELECT 100'
            ).fetchone()

            if not entry:
                err = True
                
        except sqlite3.Error:
            err = True

        assert err == False

# -------- END DATABASE --------



# -------- FUNCTIONALITIES --------

def test_water_plant(app):
    with app.app_context():
        water_qty = 100
        timestamp = time.time()
        water_util.water_plant(water_qty, timestamp)

        entry = db.get_db().execute(
            'SELECT value'
            ' FROM water'
            f' WHERE timestamp = {str(timestamp)} and value = {str(water_qty)}' 
        ).fetchone()

        assert(entry is not None)


def test_should_water_1(app):
    with app.app_context():
        response = water.get_status()
        assert response['status'] == 'fail'


def test_should_water_2(app):
    with app.app_context():
        testing_db = db.get_db()
        testing_db.execute(
            'INSERT INTO characteristics (timestamp, ideal_humidity, ideal_temperature)'
            ' VALUES (?, ?, ?) ',
            (time.time(), 70, 10)
        )
        testing_db.execute(
            'INSERT INTO humidity (timestamp, value)'
            ' VALUES (?, ?) ',
            (time.time(), 41.927)
        )
        testing_db.execute(
            'INSERT INTO temperature (timestamp, value)'
            ' VALUES (?, ?) ',
            (time.time(), 22.37)
        )
        testing_db.commit()
        
        response = water.get_status()
        assert response['status'] == 'success'


def test_get_water_qty(app):
    with app.app_context():
        testing_db = db.get_db()
        testing_db.execute(
            'INSERT INTO characteristics (timestamp, ideal_humidity, ideal_temperature)'
            ' VALUES (?, ?, ?) ',
            (time.time(), 100.0, 100.0)
        )
        testing_db.commit()
        assert isinstance(water.get_water_qty(10, 100), float)


# -------- END FUNCTIONALITIES --------


# -------- HTTP ROUTES --------

def test_set_characteristics_1(client):
    authorize(client)
    payload = {}
    response = client.post('/characteristics/set', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_set_characteristics_2(client):
    authorize(client)
    payload = {'ideal_temperature': '$sjn2', 'ideal_humidity': '12ndd[f'}
    response = client.post('/characteristics/set', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_set_characteristics_3(client):
    authorize(client)
    payload = {'ideal_temperature': 100, 'ideal_humidity': 100}
    response = client.post('/characteristics/set', json=payload, follow_redirects=True)
    assert response.status_code == 200


def test_force_water_1(client):
    authorize(client)
    payload = {}
    response = client.post('/force_water', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_force_water_2(client):
    authorize(client)
    payload = {'value': '###'}
    response = client.post('/force_water', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_force_water_3(client):
    authorize(client)
    payload = {'value': 100}
    response = client.post('/force_water', json=payload, follow_redirects=True)
    assert response.status_code == 200


def test_set_humidity_1(client):
    authorize(client)
    payload = {}
    response = client.post('/humidity/set', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_set_humidity_2(client):
    authorize(client)
    payload = {'value': 'spam'}
    response = client.post('/humidity/set', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_set_humidity_3(client):
    authorize(client)
    payload = {'value': 125}
    response = client.post('/humidity/set', json=payload, follow_redirects=True)
    assert response.status_code == 200


def test_set_temperature_1(client):
    authorize(client)
    payload = {}
    response = client.post('/temperature/set', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_set_temperature_2(client):
    authorize(client)
    payload = {'degrees': 'spam'}
    response = client.post('/temperature/set', json=payload, follow_redirects=True)
    assert response.status_code == 422


def test_set_temperature_3(client):
    authorize(client)
    payload = {'degrees': 10}
    response = client.post('/temperature/set', json=payload, follow_redirects=True)
    assert response.status_code == 200


def test_plot(client):
    authorize(client)
    response = client.get('/plot')
    assert response.status_code == 200


def test_plot_temperature(client):
    authorize(client)
    response = client.get('/plot_temperature')
    assert response.status_code == 200


def test_plot_humidity(client):
    authorize(client)
    response = client.get('/plot_humidity')
    assert response.status_code == 200

# -------- END HTTP ROUTES --------

