<!-- README template used: https://github.com/othneildrew/Best-README-Template -->

# Smart Pots
<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- ABOUT THE PROJECT -->
## About The Project
This **IoT** project aims at implementing **remote care for a potted plant** through sensors and robotics, which monitor its state.

This project was developed by Blahovici Andrei, Dumitrescu Delia, Ganea Antonio, Preda Mihai, Tudor Raluca and Ţifui Alexandru, during their third year of CS studies at University of Bucharest.

More information can be found in the [Customer Requirements Analysis Document](https://github.com/Shest-Programmistov/Smart-Pots/wiki/Customer-Requirements-Analysis-Document) wiki page.

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [SQLite](https://www.sqlite.org/index.html)
* [Eclipse Mosquitto](https://mosquitto.org/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
You should have [python3](https://www.python.org/downloads/) and [pip3](https://pypi.org/project/pip/) installed.

Also, you should have an MQTT Broker installed.

#### Linux
```sh
sudo apt-get install python3-pip
```

For installing Mosquitto MQTT Broker on Linux:
<!-- http://www.steves-internet-guide.com/install-mosquitto-linux/ -->
```sh
sudo apt-get install mosquitto
```

### Installation

#### Linux
<!-- https://tech.serhatteker.com/post/2018-12/virtualenv/ -->
1. Install virtualenv if not already installed:
```sh
sudo pip3 install virtualenv
```

2. Create a new virtual environment:
```sh
cd Smart-Pots/
virtualenv .venv
```

Note: Use `.venv` or any `$NAME` for your virtualenv.

3. Activate environment:
```sh
source .venv/bin/activate
```
and you see your `.venv` activated
```sh
(.venv) ~/Smart-Pots$
```

Note: To deactivate the environment, simply use `deactivate`.

4. Install libraries
```sh
pip3 install -r requirements.txt
```

5. To switch Flask to the development environment and enable debug mode, set `FLASK_ENV`:
```sh
export FLASK_ENV=development
```

6. Initialize (or reinitialize) database:
```sh
flask init-db
```

7. **Start the MQTT Broker service**. If Mosquitto is used, run:
```sh
sudo service mosquitto start 
```
To test if it is running use the `netstat –at` command. You should see the Mosquitto broker running on port 1883.

To stop the service, use `sudo service mosquitto stop`.

8. Running the application.
The proper way to run the application is:
```sh
python3 app.py
```
This way, we make sure that SocketIO is used, as Flask is wrapped in SocketIO.

Note: To only run the Flask app (no MQTT communication), just use:
```sh
flask run
```

9. Run the MQTT subscriber to check that data is successfully received.
```sh
python3 mqtt_comms_sub.py
```

<!-- USAGE EXAMPLES -->
## Usage
The Swagger API can be accessed at
```
http://127.0.0.1:5000/api/docs
```

<!-- CONTRIBUTING -->
## Contributing

Any contributions are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[contributors-url]: https://github.com/Shest-Programmistov/Smart-Pots/graphs/contributors

[stars-shield]: https://img.shields.io/github/stars/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[stars-url]: https://github.com/Shest-Programmistov/Smart-Pots/stargazers

[issues-shield]: https://img.shields.io/github/issues/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[issues-url]: https://github.com/Shest-Programmistov/Smart-Pots/issues

[license-shield]: https://img.shields.io/github/license/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[license-url]: https://github.com/Shest-Programmistov/Smart-Pots/blob/main/LICENSE
