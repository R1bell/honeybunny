from __future__ import annotations

from typing import Optional

from app.db import DB as db


class User(db.Model):
    __tablename__: str = "User"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    login = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(32))
    goods = db.relationship(
        "Busket",
        backref="user",
        lazy="dynamic",
        foreign_keys="Busket.user_id"
    )

    def __repr__(self) -> str:
        return "{} {}".format(self.firstName, self.lastName)

    @staticmethod
    def is_exists_login(login: Optional[None]) -> bool:
        return db.session\
            .query(User.id).\
            filter_by(login=login)\
            .scalar() is not None

    @staticmethod
    def is_exists_email(email: str) -> bool:
        return db.session\
            .query(User.id)\
            .filter_by(email=email)\
            .scalar() is not None

    @property
    def commit(self) -> User:
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def log_in(login: str, password: str) -> User:
        return User.query.filter_by(login=login, password=password).first()
