<!-- README template used: https://github.com/othneildrew/Best-README-Template -->

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<h3 align="center">Smart Pots</h3>
  <p align="center">
    We take care of your plant so you don't have to.
  </p>


<!-- ABOUT THE PROJECT -->
## About The Project
This **IoT** project aims at implementing **remote care for a potted plant** through sensors and robotics, which monitor its state.

This project was developed by Blahovici Andrei, Dumitrescu Delia, Ganea Antonio, Preda Mihai, Tudor Raluca and Ţifui Alexandru, during their third year of CS studies at University of Bucharest, under guidance of Rareș Cristea.

The documentation can also be found at [Smart Pots Documentation](https://smart-pots.readthedocs.io/).

More information can be found in the [Customer Requirements Analysis Document](https://github.com/Shest-Programmistov/Smart-Pots/wiki/Customer-Requirements-Analysis-Document) wiki page.

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [SQLite](https://www.sqlite.org/index.html)
* [Eclipse Mosquitto](https://mosquitto.org/)
* [Flask-MQTT](https://flask-mqtt.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/6.2.x/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
You should have [python3](https://www.python.org/downloads/) and [pip3](https://pypi.org/project/pip/) installed.
<!--```sh
sudo apt-get install python3-pip
```-->

Also, you should have an MQTT Broker installed.

### Mosquitto MQTT Broker Installation

For installing Mosquitto MQTT Broker, go to their [official website](https://mosquitto.org/download/) and download and install the Mosquitto Broker for your OS.

#### For Ubuntu/Debian:
<!-- http://www.steves-internet-guide.com/install-mosquitto-linux/ -->
```sh
sudo apt-get install mosquitto
```
To check whether the service is running or not and to start it, run:
```sh
sudo systemctl status mosquitto # Checking if the service is running
sudo systemctl start mosquitto # Start the service
```

#### For Mac: 
Install Mosquitto on Mac OS using Homebrew:
```bash
brew install mosquitto
```

### Installation

<!-- https://tech.serhatteker.com/post/2018-12/virtualenv/ -->
1. Install virtualenv if not already installed. 

On Linux, run:
```sh
sudo pip3 install virtualenv
```

2. Create a new virtual environment:
```sh
cd Smart-Pots/
virtualenv .venv
```

Note: Use `.venv` or any `$NAME` for your virtualenv.

3. Activate the environment:
```sh
source .venv/bin/activate
```
and you see your `.venv` activated
```sh
(.venv) ~/Smart-Pots$
```

Note: To deactivate the environment, simply use `deactivate`.

4. Install the required libraries:
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

<!-- USAGE EXAMPLES -->
## Usage

1. **Start the MQTT Broker service**. The Broker represents an intermediary entity that enables the MQTT clients to communicate.

If Mosquitto is used, run:
```sh
sudo service mosquitto start
```
To test if it is running use the `netstat –at` command. You should see the Mosquitto broker running on port 1883.

To stop the service, use `sudo service mosquitto stop`.

2. Running the application.
The proper way to run the application is:
```sh
python3 app.py
```
This way, we make sure that SocketIO is used, as Flask is wrapped in SocketIO.

Note: To only run the Flask app (no MQTT communication), just use:
```sh
flask run
```

3. [Optional] Run the MQTT subscriber to check that data is successfully received.
```sh
python3 mqtt_comms_sub.py
```

## Test
To run the tests, simply execute:
```sh
pytest
```

To measure the code coverage, run:
```sh
coverage run -m pytest
```
and then use coverage report to report on the results:
```sh
coverage report -m
```
For a nicer presentation, use `coverage html` to get annotated HTML listings detailing missed lines.

## Developer Tools
### OpenAPI
We used the [OpenAPI Initiative (OAI)](https://www.openapis.org/) to specify what our API can do. 

The Swagger UI can be accessed at:
```
http://127.0.0.1:5000/api/docs
```

### AsyncAPI
<!-- https://nordicapis.com/how-to-write-your-first-asyncapi-specification/ -->
The [AsyncAPI Specification](https://www.asyncapi.com/docs/specifications/v2.0.0) is a comprehensive specification language for describing asynchronous messaging APIs. 

<!-- https://github.com/asyncapi/html-template -->

If AsyncAPI Generator is not installed, you can install it by running:
```sh
npm install -g @asyncapi/generator
```

Then, run:
```sh
ag water.yml @asyncapi/html-template -o output
```

### Read the Docs Documentation
<!-- https://towardsdatascience.com/how-to-set-up-your-python-project-docs-for-success-aab613f79626 -->

Using [Read the Docs](https://readthedocs.org/), the documentation (available at https://smart-pots.readthedocs.io/) was set up to be built automatically on each new release. 

The docs was done using [Sphinx](https://www.sphinx-doc.org/en/master/). Check out the `docs` directory in the top level of the project directory. `docs/conf.py` controls how Sphinx runs when the docs are built.

The Makefile that was generated by Sphinx controls how shortcut commands that start with make operate. 
Run
```sh
make html
```
from the command line to manually build the docs - then, in `docs->build_->html` directory you should see `index.html`.

Note: we followed the [Style guide for Sphinx-based documentations](https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html).

<!-- Bug identification -->
## Bug identification

Bug identification was done by using the [Restler](https://github.com/microsoft/restler-fuzzer) tool. To use this run the following commands (these were tested on Linux, but if you want to test on other platforms check out the official documentation):

1. Download the official repo
```sh
git clone https://github.com/microsoft/restler-fuzzer.git && cd restler-fuzzer
```

2. Create the folder for the Restler binaries
```sh
mkdir ../restler_bin
```

3. Build the Restler project
```sh
python ./build-restler.py --dest_dir ../restler_bin
```

4. Delete the downloaded repo
```sh
cd .. && rm restler-fuzzer
```

5. Go to the folder where the binaries have been built
```sh
cd restler_bin
```

6. Compile the neccessary files for Restler
```sh
dotnet ./restler/Restler.dll compile --api_spec ./swagger.json
```

7. Run it (for other modes check out the official documentation)
```sh
dotnet ./restler/Restler.dll test --grammar_file grammar.py --dictionary_file dict.json --settings engine_settings.json --no_ssl
```

### Identified bugs so far (and fixed):

* Accepted temperature and humidity values are real numbers, but at first they were checked for integers (non-floating numbers)
* Empty form bodies made all endpoints throw exceptions


<!-- LICENSE -->
## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.


<!-- CONTRIBUTING -->
## Contributing

Any contributions are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
The following list includes resources we found helpful and would like to give credit to:
* The Software Engineering Courses provided by University of Bucharest;
* [raresito/SmartBed-RESTApi-example](https://github.com/raresito/SmartBed-RESTApi-example);
* [Flask-MQTT Package Usage](https://flask-mqtt.readthedocs.io/en/latest/usage.html);
* [Getting Started with OpenAPI Tools](https://swagger.io/tools/open-source/getting-started/)
* [asyncapi/html-template](https://github.com/asyncapi/html-template).
* [How to Write Your First AsyncAPI Specification](https://nordicapis.com/how-to-write-your-first-asyncapi-specification/)
* [How to Set Up Your Python Project Docs for Success🎉](https://towardsdatascience.com/how-to-set-up-your-python-project-docs-for-success-aab613f79626)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[contributors-url]: https://github.com/Shest-Programmistov/Smart-Pots/graphs/contributors

[stars-shield]: https://img.shields.io/github/stars/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[stars-url]: https://github.com/Shest-Programmistov/Smart-Pots/stargazers

[issues-shield]: https://img.shields.io/github/issues/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[issues-url]: https://github.com/Shest-Programmistov/Smart-Pots/issues

[license-shield]: https://img.shields.io/github/license/Shest-Programmistov/Smart-Pots.svg?style=for-the-badge
[license-url]: https://github.com/Shest-Programmistov/Smart-Pots/blob/main/LICENSE
