from __future__ import annotations

from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.db import DB as db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wayOfPaiment = db.Column(db.String(128))
    oddMoney = db.Column(db.String(128))
    address = db.Column(db.String(128))
    porch = db.Column(db.String(128))
    floor = db.Column(db.String(128))
    apartment = db.Column(db.String(128))
    comment = db.Column(db.Text)
    firstName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    email = db.Column(db.String(128))
    login = db.Column(db.String(128))

    @property
    def commit(self) -> Order:
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def all(login) -> List[Order]:
        return Order.query.filter_by(login=login).all()
