# flake8: noqa
from os import environ as env

DEBUG = True
SECRET_KEY = "FKO2-F0OJ-O]j4fgj"
SQLALCHEMY_DATABASE_URI = "postgres://txlhebbodfxvkw:0522896a30edfeb8599366e2fbd459a2d21f9c3bc88d0bfaa348a9a4cf171400@ec2-3-229-210-93.compute-1.amazonaws.com:5432/d3sbaii4qrobi9"
SQLALCHEMY_TRACK_MODIFICATIONS = True
RESTPLUS_MASK_SWAGGER = False
JWT_SECRET_KEY = "hn9grzAnEQBsEE9E"
LOG_TO_STDOUT = env.get('LOG_TO_STDOUT')
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'honeybunnycandyshop@gmail.com'
MAIL_DEFAULT_SENDER = 'honeybunnycandyshop@gmail.com'
MAIL_PASSWORD = 'SGzHEqB9VqcVLrv'
