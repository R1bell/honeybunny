from flask import Flask
from flask_mail import  Mail

MAIL = Mail()


def create_mail(app: Flask) -> Mail:
    MAIL.init_app(app)
    return MAIL
