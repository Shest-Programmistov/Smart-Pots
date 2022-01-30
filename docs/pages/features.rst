========
Features
========

****************
Overall Workflow
****************
The smart pot acts as the "publisher" - constantly broadcasting the amount of water that should be provided to the plant.

Two threads are used - for HTTP and MQTT requests respectively.

In regards to MQTT, the Broker represents an intermediary entity that enables the MQTT clients to communicate.

A subscriber mock script is also provided for testing purposes.

**********
Tools Used
**********
For the HTTP connection, we are using the Flask library.
For the MQTT connection, we use the flask_mqtt library. Also, for mocking the subscriber, `paho-mqtt <https://pypi.org/project/paho-mqtt/>`_ is used.
For a DB system, we use SQLite - a fully open-source RDBMS known for its portability and reliability.

**********************
Temperature Monitoring
**********************

.. automodule:: http_routes.temperature
   :members:

*******************
Humidity Monitoring
*******************

.. automodule:: http_routes.humidity
   :members:

******************
Automatic Watering
******************

.. automodule:: http_routes.water_api
   :members:

***************
Manual Watering
***************
Smart Pots also provides a manual watering functionality.

.. automodule:: http_routes.force_water
   :members:

*******************
Watering Statistics
*******************

.. automodule:: http_routes.plot
   :members:
