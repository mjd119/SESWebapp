-- See https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
DROP TABLE IF EXISTS user;

CREATE TABLE user (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT NOT NULL UNIQUE,
       first_name TEXT NOT NULL,
       last_name TEXT NOT NULL,
       sex char(1) NOT NULL,
       birthday TEXT NOT NULL
);

