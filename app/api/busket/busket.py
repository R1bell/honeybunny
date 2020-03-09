from dataclasses import dataclass
from typing import Optional

from flask_jwt_extended import jwt_required
from flask_restplus import Resource

from app.api.busket.models import item_amount, item_model, item_with_good
from app.api.busket.namespace import BUSKET_NAMESPACE as api
from app.api.responses import get_codes
from app.db import DB as db
from app.models import Busket, Good, User

auth = {
    "Authorization": {
        "in": "header"
    }
}


@api.route("/")
class Buskets(Resource):
    @api.expect(item_model, validate=True)
    @api.doc(responses=get_codes(200, 401, 409), security="apiKey", params=auth)
    @jwt_required
    def post(self):
        return "success" if Busket(**api.payload).commit else api.abort(409)


@api.route("/<item_id>")
class BusketsByItemId(Resource):
    @api.expect(item_amount, validate=True)
    @api.doc(responses=get_codes(200, 404), security="apiKey", params=auth)
    @jwt_required
    def put(self, item_id):
        item: Optional[Busket] = Busket.query.filter_by(id=item_id).first()
        if item:
            item.update(api.payload["amount"])
            return "success"
        api.abort(404)

    @api.doc(responses=get_codes(200, 404), security="apiKey", params=auth)
    def delete(self, item_id):
        return "success" if Busket.delete(id=item_id) else api.abort(404)


@api.route("/<user_id>")
class BusketsByUserId(Resource):
    @api.marshal_list_with(item_with_good, mask=None)
    @api.doc(responses=get_codes(404), security="apiKey", params=auth)
    def get(self, user_id: str):
        return [{
            "id": good[0],
            "amount": good[1],
            "good": {
                "id": good[2],
                "name": good[3],
                "weight": good[4],
                "description": good[5],
                "measure": good[6],
                "price": good[7],
                "category": good[8]
            }
        } for good in db.session.execute(
            """SELECT
                "Busket".id as item_id,
                "Busket".amount as amount,
                "Good".id as "id",
                "Good".name as name,
                "Good".weight as weight,
                "Good".description as description,
                "Good".measure as measure,
                "Good".price as price,
                "Category".name as category
            FROM "Busket"
            JOIN "Good" ON "Busket".good_id="Good".id
            JOIN "Category" ON "Good".category_id="Category".id
            WHERE "Busket".user_id={}""".format(user_id))]
