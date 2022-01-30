.. Smart Pots documentation master file, created by
   sphinx-quickstart on Sun Jan 23 13:41:36 2022.
   You can adapt this file completely to your liking, 
   but it should at least contain the root `toctree` 
   directive.

Welcome to Smart Pots's documentation!
======================================

Smart Pots is an IoT project implementing remote care for a potted plant, 
through sensors and robotics which monitor its state. 

|pot_img|

Please refer to :ref:`installation` to get started with using Smart Pots.

Once you've :doc:`installed <pages/installation>` *Smart Pots*, we recommend 
reading the :doc:`tutorial <pages/tutorial>`.

For a complete list of features, see :doc:`features <pages/features>`.

The code can be found on GitHub at `Shest-Programmistov/Smart-Pots <https://github.com/Shest-Programmistov/Smart-Pots>`_.
Data has been taken from `IoTsec/Room-Climate-Datasets <https://github.com/IoTsec/Room-Climate-Datasets>`_.

**********
Tools Used
**********
* For the HTTP connection, we are using the `Flask <https://flask.palletsprojects.com/en/2.0.x/>`_ library.
* For the MQTT connection, the `Flask-MQTT extension <https://flask-mqtt.readthedocs.io/en/latest/>`_ is used. Also, for mocking the MQTT subscriber, `paho-mqtt <https://pypi.org/project/paho-mqtt/>`_ is used.
* The database is built using `SQLite <https://www.sqlite.org/index.html>`_ - a fully open-source RDBMS.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pages/installation
   pages/tutorial
   pages/features


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
