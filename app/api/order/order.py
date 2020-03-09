from flask_restplus import Resource
from flask_restplus import fields
from flask_jwt_extended import jwt_required

from app.api.order.models import order_model, order_id
from app.api.order.namespace import ORDER_NAMESPACE as api
from app.api.responses import get_codes
from app.models.order import Order

auth = {
    "Authorization": {
        "in": "header"
    }
}


@api.route("/")
class Orders(Resource):
    @jwt_required
    @api.marshal_with(order_id, mask=None)
    @api.expect(order_model, validate=True)
    @api.doc(responses=get_codes(200), security="apiKey", params=auth)
    def post(self):
        return Order(**api.payload).commit
