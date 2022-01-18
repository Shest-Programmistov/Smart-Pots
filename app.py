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
import auth
import temperature
import humidity
import force_water
import water
import water_api
import characteristics
import plot

# Necessary monkey-patch so that SocketIO successfully works.
eventlet.monkey_patch()

app = None  # Flask app
mqtt = None # MQTT wrapper over app
socketio = None
thread = None


def create_app():
    """Creates Flask main application."""
    global app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/')
    def hello_world():
        """Start the periodic publishing after the root endpoint is called."""
        # It's not the best, nor cleanest approach, but will have to refactor it.
        # What is important is that the background_thread function is called on
        # a separate thread, so that publishing can happen while simultaneously
        # HTTP endpoints are also functional.

        global thread
        if thread is None:
            thread = Thread(target=background_thread)
            thread.daemon = True
            thread.start()
        return 'Hello World!'

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

    db.init_app(app)
    app.register_blueprint(swaggerui_blueprint)
    app.register_blueprint(temperature.bp)
    app.register_blueprint(water_api.bp)
    app.register_blueprint(humidity.bp)
    app.register_blueprint(force_water.bp)
    app.register_blueprint(characteristics.bp)
    app.register_blueprint(plot.bp)

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
    mqtt = Mqtt(app)
    global socketio
    socketio = SocketIO(app, async_mode="eventlet")

    return mqtt


def background_thread():
    """Starts MQTT publishing.

    At every second, publish the status (TODO define what to publish) to broker.
    """
    while True:
        time.sleep(5)
        # Using app context is required because the get_status() functions
        # requires access to the db.
        with app.app_context():
            message = json.dumps(water.get_status(), default=str)
        # Publish
        mqtt.publish('python/mqtt', message)


# App will now have to be run with `python app.py` as flask is now wrapped in socketio.
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
