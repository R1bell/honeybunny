from flask_restplus import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.order.models import order_model, order_id, new_order
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
    @api.expect(new_order, validate=True)
    @api.doc(responses=get_codes(200), security="apiKey", params=auth)
    def post(self):
        return Order(**api.payload, login=get_jwt_identity()).commit

    @jwt_required
    @api.marshal_list_with(order_model, mask=None)
    @api.doc(responses=get_codes(200), security="apiKey", params=auth)
    def get(self):
        return Order.all(get_jwt_identity())
