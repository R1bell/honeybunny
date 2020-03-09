# flake8: noqa
from os import environ as env

DEBUG = True
SECRET_KEY = "FKO2-F0OJ-O]j4fgj"
SQLALCHEMY_DATABASE_URI = env.get("DATABASE_URL") or "postgresql://postgre:postgre@postgresql:5432/honeybunny"
SQLALCHEMY_TRACK_MODIFICATIONS = True
RESTPLUS_MASK_SWAGGER = False
JWT_SECRET_KEY = "hn9grzAnEQBsEE9E"
LOG_TO_STDOUT = env.get('LOG_TO_STDOUT')
