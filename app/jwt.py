from flask import Flask
from flask_jwt_extended import JWTManager

JWT: JWTManager = JWTManager()


def create_jwt(app: Flask) -> JWTManager:
    JWT.init_app(app)
    return JWT
