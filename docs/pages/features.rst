========
Features
========

****************
Overall Workflow
****************
The smart pot acts as the "publisher".

Two threads are used - for HTTP and MQTT requests respectively.

In regards to MQTT, the Broker represents an intermediary entity that enables the MQTT clients to communicate.

A subscriber mock script is also provided for testing purposes.

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
