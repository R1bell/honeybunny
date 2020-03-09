from os import system

from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from os import environ as env

from app.admin import create_admin
from app.app import create_app
from app.db import create_db
from app.jwt import create_jwt
from app.models import Busket, Category, Good, User, Order

app: Flask = create_app()
CORS(app)
db: SQLAlchemy = create_db(app)
jwt: JWTManager = create_jwt(app)
manager: Manager = Manager(app)
migrate: Migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
admin: Admin = create_admin(app)


@manager.command
def run():
    system('python manage.py db upgrade')
    app.run(debug=True, host="0.0.0.0", port=int(env.get("PORT", 5000)))


if __name__ == '__main__':
    manager.run()
