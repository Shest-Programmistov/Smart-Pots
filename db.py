import sqlite3

import click
from flask import g
from flask.cli import with_appcontext
from flask import current_app

import os
import csv
import tqdm


def get_db():
    """Opens a connection to the SQLite database file, if not yet
    opened, and returns the database."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DB_PATH'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with open('schema.sql', encoding='utf8') as f:
        db.executescript(f.read())
    
    if current_app.config['DB_PATH'] == 'flaskr.sqlite':
        populate_database(db)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def populate_database(db):
    DATA_PATH = 'data/datasets-location_B'
    csv_file_names = os.listdir(DATA_PATH)
    print("Populating database")
    for csv_file_name in tqdm.tqdm(csv_file_names):
        with open(os.path.join(DATA_PATH, csv_file_name), newline='') as csv_file:
            rows = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in rows:
                _, timestamp, _, _, temperature, humidity, _, _, _, _, _, _ = row
                db.execute(
                    'INSERT INTO temperature (timestamp, value)'
                    ' VALUES (?, ?) ',
                    (int(timestamp[:-1]), float(temperature[:-1]))
                )
                db.execute(
                    'INSERT INTO humidity (timestamp, value)'
                    ' VALUES (?, ?) ',
                    (int(timestamp[:-1]), float(humidity[:-1]))
                )
                db.commit()
