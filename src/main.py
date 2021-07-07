# This is a sample Python script.
# See https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/ for initial setup
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Blueprint, render_template, request
from flask_cors import cross_origin
from .db import get_db
main = Blueprint('main', __name__)

# a simple page that says hello
@main.route('/hello')
@main.route('/')  # Default landing page
def hello():
    database = get_db()
    username = "chilldude42"
    first_name = "John"
    last_name = "Smith"
    sex = "Male"
    birthday = "02/29/1955"
    # See https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#insert-on-conflict-upsert
    database.execute("INSERT INTO user (username, first_name, last_name, sex, birthday) VALUES (?,?,?,?,?) ON CONFLICT DO NOTHING",
                     (username, first_name, last_name, sex, birthday))
    database.commit()

    users = database.execute("SELECT * FROM user")

    return render_template('hello.html', users=users)
# Post method for hello page (root page)
@main.route('/hello', methods=['POST'])
@main.route('/', methods=['POST'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
def hello_post():
    if request.method == 'POST':
        database = get_db()
        username = request.form.get('username')
        print(username)
        first_name = request.form.get('first_name')
        print(first_name)
        last_name = request.form.get('last_name')
        print(last_name)
        sex = request.form.get('sex')
        print(sex)
        birthday = request.form.get('birthday')
        print(birthday)
        database.execute("INSERT INTO user (username, first_name, last_name, sex, birthday) VALUES (?,?,?,?,?) ON CONFLICT DO NOTHING",
                         (username, first_name, last_name, sex, birthday))
        database.commit()
        users = database.execute("SELECT * FROM user")
        return render_template('hello.html', users=users)

@main.route('/users')
def users():
    database = get_db()
    users = database.execute("SELECT * FROM user")
    return render_template('users.html', users=users)