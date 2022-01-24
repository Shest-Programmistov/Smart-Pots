============
Installation
============

#############
Prerequisites
#############

:Precondition: `python3 <https://www.python.org/downloads/>`_ and 
    `pip3 <https://pypi.org/project/pip/>`_ are installed. Also, you should have an MQTT Broker installed.

*****
Linux
*****
For installing `pip3 <https://pypi.org/project/pip/>`_:
::
    sudo apt-get install python3-pip

For installing `Mosquitto MQTT Broker <https://mosquitto.org/>`_:
::
    sudo apt-get install mosquitto

############
Installation
############

*****
Linux
*****
1. Install virtualenv if not already installed:
::
    sudo pip3 install virtualenv

2. Create a new virtual environment:
::
    cd Smart-Pots/
    virtualenv .venv

Note: Use `.venv` or any `$NAME` for your virtualenv.

3. Activate environment:
::
    source .venv/bin/activate

and you should see your `.venv` activated
::
    (.venv) ~/Smart-Pots$

Note: To deactivate the environment, simply use `deactivate`.

4. Install libraries
::
    pip3 install -r requirements.txt

5. To switch Flask to the development environment and enable debug mode, set `FLASK_ENV`:
::
    export FLASK_ENV=development

6. Initialize (or reinitialize) database:
::
    flask init-db
