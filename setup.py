from setuptools import setup

setup(
    name='Smart Pots',
    version='1.0.0',
    description='IoT project implementing remote care for a potted plant through sensors.',
    long_description="See https://github.com/Shest-Programmistov/Smart-Pots",
    url='https://github.com/Shest-Programmistov/Smart-Pots',
    author='Blahovici Andrei, Dumitrescu Delia, Ganea Antonio, Preda Mihai, Tudor Raluca and Ţifui Alexandru',
    license='APACHE-2.0',
    install_requires=[
        'eventlet==0.32.0',
        'Flask==2.0.2',
        'Flask-MQTT==1.1.1',
        'Flask-SocketIO==5.1.1',
        'pytest==6.2.5',
        'Sphinx==4.4.0',
        'flask-swagger==0.2.14',
        'flask-swagger-ui==3.36.0',
        'matplotlib==3.5.1',
        'pandas==1.3.5',
        'sphinx-rtd-theme==1.0.0',
        'tqdm==4.62.3'
    ],
    python_requires='>=3.7',
)
