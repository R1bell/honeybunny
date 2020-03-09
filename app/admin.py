from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.db import DB as db
from app.models import Busket, Category, Good, Order, User

ADMIN: Admin = Admin()


def create_admin(app: Flask) -> Admin:
    ADMIN = Admin(app)
    ADMIN.add_view(ModelView(User, db.session))
    ADMIN.add_view(ModelView(Good, db.session))
    ADMIN.add_view(ModelView(Category, db.session))
    ADMIN.add_view(ModelView(Busket, db.session))
    ADMIN.add_view(ModelView(Order, db.session))
    return ADMIN
