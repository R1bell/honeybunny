from flask import Flask

from app import config
from app.api.api import create_api


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    blueprint_api = create_api()
    app.register_blueprint(blueprint_api)

    return app
