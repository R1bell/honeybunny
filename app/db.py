from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB: SQLAlchemy = SQLAlchemy()


def create_db(app: Flask) -> SQLAlchemy:
    DB.init_app(app)
    return DB
