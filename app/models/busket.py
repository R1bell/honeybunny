from sqlalchemy import UniqueConstraint
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.db import DB as db


class Busket(db.Model):
    __tablename__ = "Busket"
    __table_args__ = (UniqueConstraint(
        'user_id',
        'good_id',
        name='unique_user_good'),)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    good_id = db.Column(db.Integer, db.ForeignKey("Good.id"))
    amount = db.Column(db.Integer)

    def __repr__(self):
        return "user - {}\ngood - {}\namount - {}"

    @property
    def commit(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    def update(self, amount: int):
        self.amount = amount
        db.session.commit()

    @staticmethod
    def delete(id: int) -> bool:
        try:
            db.session.delete(Busket.query.filter_by(id=id).first())
            db.session.commit()
            return True
        except UnmappedInstanceError:
            return False

    @staticmethod
    def delete_all(user_id: int) -> bool:
        try:
            Busket.query.filter_by(user_id=user_id).delete()
            return True
        except UnmappedInstanceError:
            return False
