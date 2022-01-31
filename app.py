from flask import Flask, jsonify
from threading import Thread
from flask_mqtt import Mqtt
# Import SockeIO, which allows us to send messages to
# an MQTT client using Flask syntax.
from flask_socketio import SocketIO
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import eventlet
import json
import time

import db
import water
import http_routes.auth as auth
import http_routes.temperature as temperature
import http_routes.humidity as humidity
import http_routes.force_water as force_water
import http_routes.characteristics as characteristics
import http_routes.plot as plot
import http_routes.frontend as frontend

# Necessary monkey-patch so that SocketIO successfully works.
eventlet.monkey_patch()

app = None  # Flask app
mqtt = None  # MQTT wrapper over app
socketio = None
thread = None


def create_app(testing=False, db_path='flaskr.sqlite'):
    """Creates Flask main application."""
    global app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_PATH=db_path
    )
    if testing:
        app.config['TESTING'] = True

    # Swagger route
    @app.route("/spec")
    def spec():
        return jsonify(swagger(app))

    # Swagger
    # URL for exposing Swagger UI (without trailing '/')
    SWAGGER_URL = '/api/docs'
    # Our API url (can of course be a local resource)
    API_URL = 'http://127.0.0.1:5000/spec'

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI config overrides
            'title': "Smart Pot"
        }
    )

    if not testing:
        db.init_app(app)

    app.register_blueprint(swaggerui_blueprint)
    app.register_blueprint(auth.bp)
    app.register_blueprint(temperature.bp)
    app.register_blueprint(humidity.bp)
    app.register_blueprint(force_water.bp)
    app.register_blueprint(characteristics.bp)
    app.register_blueprint(plot.bp)
    app.register_blueprint(frontend.bp)

    return app


def create_mqtt_app():
    """Set-up and create connection to MQTT broker."""
    # Define configuration values for the MQTT broker, so that
    # the application knows to which broker to send the info.

    # Use the default broker from Mosquitto
    app.config['MQTT_BROKER_URL'] = 'localhost'
    # Set the default port for non-TLS connection.
    app.config['MQTT_BROKER_PORT'] = 1883
    # Set the username here if you need authentication for the broker.
    app.config['MQTT_USERNAME'] = ''
    # Set the password here if the broker demands authentication.
    app.config['MQTT_PASSWORD'] = ''
    # Set the time interval for sending a ping to the broker to 5 seconds.
    app.config['MQTT_KEEPALIVE'] = 5
    # Set TLS to disabled for testing purposes.
    app.config['MQTT_TLS_ENABLED'] = False

    global mqtt
    # Connect to MQTT broker.
    mqtt = Mqtt(app)
    global socketio
    socketio = SocketIO(app, async_mode="eventlet")

    """Start the periodic publishing after the root endpoint is called."""

    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()

    return mqtt


def background_thread():
    """Starts MQTT publishing.

    At every second, publish the water status to broker.
    """
    while True:
        time.sleep(5)
        # Using app context is required because the get_status() functions
        # requires access to the db.
        with app.app_context():
            message = json.dumps(water.get_status(), default=str)
        # Publish on 'python/mqtt' topic.
        mqtt.publish('python/mqtt', message)


# App will now have to be run with `python app.py`, 
# as Flask is now wrapped in socketio.
def run_socketio_app():
    create_app()
    create_mqtt_app()
    socketio.run(
        app,
        host='localhost',
        port=5000,
        use_reloader=False,
        debug=True)


if __name__ == '__main__':
    run_socketio_app()
