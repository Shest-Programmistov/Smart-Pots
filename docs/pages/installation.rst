============
Installation
============

#############
Prerequisites
#############

:Precondition: `python3 <https://www.python.org/downloads/>`_ and 
    `pip3 <https://pypi.org/project/pip/>`_ are installed. Also, you should have an MQTT Broker installed.

**********************************
Mosquitto MQTT Broker Installation
**********************************

For installing Mosquitto MQTT Broker, go to their 
`official website <https://mosquitto.org/download/>`_ 
and download and install the Mosquitto Broker for your OS.

For Ubuntu/Debian:
==================
Run:
::
    sudo apt-get install mosquitto

To check whether the service is running or not and to start it, run:
::
    sudo systemctl status mosquitto # Checking if the service is running
    sudo systemctl start mosquitto # Start the service

For Mac: 
========
Install Mosquitto on Mac OS using Homebrew:
::
    brew install mosquitto


############
Installation
############

1. Install virtualenv if not already installed:

On Linux, run:
::
    sudo pip3 install virtualenv

2. Create a new virtual environment:
::
    cd Smart-Pots/
    virtualenv .venv

Note: Use `.venv` or any `$NAME` for your virtualenv.

3. Activate the environment:
::
    source .venv/bin/activate

and you should see your `.venv` activated
::
    (.venv) ~/Smart-Pots$

Note: To deactivate the environment, simply use `deactivate`.

4. Install the required libraries:
::
    pip3 install -r requirements.txt

5. To switch Flask to the development environment and enable debug mode, set `FLASK_ENV`:
::
    export FLASK_ENV=development

6. Initialize (or reinitialize) database:
::
    flask init-db
