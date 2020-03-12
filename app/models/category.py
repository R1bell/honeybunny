from __future__ import annotations

from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.db import DB as db
from app.models.good import Good


class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    goods = db.relationship("Good", backref="category", lazy="dynamic")

    def __repr__(self):
        return self.name

    def commit(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def get_all_goods(category_name: str) -> List[Good]:
        goods = Category.query.filter_by(name=category_name).first()
        return goods.goods.all() if goods else []

    @staticmethod
    def all() -> List[Category]:
        return Category.query.all()

    @staticmethod
    def first(**kwargs) -> Category:
        return Category.query.filter_by(**kwargs).first()

    @staticmethod
    def delete(**kwargs) -> bool:
        try:
            db.session.delete(Category.query.filter_by(**kwargs).first())
            db.session.commit()
            return True
        except UnmappedInstanceError:
            return False
