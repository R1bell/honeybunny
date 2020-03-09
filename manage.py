from os import system

from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from app.admin import create_admin
from app.app import create_app
from app.db import create_db
from app.jwt import create_jwt
from app.models import Busket, Category, Good, User, Order

app: Flask = create_app()
CORS(app)
db: SQLAlchemy = create_db(app)
jwt: JWTManager = create_jwt(app)
migrate: Migrate = Migrate(app, db)
admin: Admin = create_admin(app)
