# See https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
# See https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
# Directions for linux machine (I believe you use set instead of export on Windows)
# Install flask, requests,  (pip if on windows)
# export FLASK_APP=SES-WebApp/src
# export FLASK_ENV=development
# flask init-db
# flask run --host 127.0.0.1 --port=5001
# NOT NEEDED BELOW
# npm init -y
# npm install babel-cli@6 babel-preset-react-app@3
import os
from flask import Flask
from src.db import get_db
from flask_cors import CORS
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/*": {"origins": "*"}}) # See https://stackoverflow.com/a/42526202
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # @app.route('/hello')
    # @app.route('/') # Default landing page
    # def hello():
    #     database = get_db()
    #     first_name = "John"
    #     last_name = "Smith"
    #     sex = "Male"
    #     birthday = "02/29/1955"
    #     # See https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#insert-on-conflict-upsert
    #     database.execute("INSERT INTO user (first_name, last_name, sex, birthday) VALUES (?,?,?,?) ON CONFLICT DO NOTHING",
    #                      (first_name, last_name, sex, birthday))
    #     database.commit()

        # users = database.execute("SELECT * FROM user")

        # return render_template('hello.html', users=users)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint) # Associate application with functions from main.py

    from . import db
    # Initialize database
    db.init_app(app)

    return app
