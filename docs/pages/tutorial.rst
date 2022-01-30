========
Tutorial
========

First, refer to :ref:`installation` for setting up Smart Pots.
After having installed successfully the requirements, follow the next steps:

****************
Running on Linux
****************

1. **Start the MQTT Broker service**. The Broker represents an intermediary entity that enables the MQTT clients to communicate.

If Mosquitto is used, run:
::
    sudo service mosquitto start 

To test if it is running use the `netstat –at` command. You should see the Mosquitto broker running on port 1883.

To stop the service, use `sudo service mosquitto stop`.

2. Running the application.
The proper way to run the application is:
::
    python3 app.py

This way, we make sure that SocketIO is used, as Flask is wrapped in SocketIO.

Note: To only run the Flask app (no MQTT communication), just use:
::
    flask run


[Optional] 3. Run the MQTT subscriber to check that data is successfully received.
::
    python3 mqtt_comms_sub.py


*******
Testing
*******
To run the tests, simply execute:
::
    pytest

To measure the code coverage, run:
::
    coverage run -m pytest

and then use coverage report to report on the results:
::
    coverage report -m

For a nicer presentation, use `coverage html` to get annotated HTML listings detailing missed lines.


***************
Developer Tools
***************

OpenAPI
=======
We used the `OpenAPI Initiative (OAI) <https://www.openapis.org/>`_ to specify what our API can do. 

The Swagger API can be accessed at:
::
    http://127.0.0.1:5000/api/docs

AsyncAPI
========
The `AsyncAPI Specification <https://www.asyncapi.com/docs/specifications/v2.0.0>`_ is a comprehensive specification language for describing asynchronous messaging APIs. 

If AsyncAPI Generator is not installed, you can install it by running:
::
    npm install -g @asyncapi/generator

Then, run:
::
    ag water.yml @asyncapi/html-template -o output
