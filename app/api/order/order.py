from typing import List
from datetime import date

from flask_mail import Message
from flask_restplus import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.order.models import order_model, order_id, new_order
from app.api.order.namespace import ORDER_NAMESPACE as api
from app.api.responses import get_codes
from app.models.order import Order
from app.mail import MAIL as mail

auth = {
    "Authorization": {
        "in": "header"
    }
}

body_template = """
Здравствуйте, {firstName}!
Благодарим вас за покупку в нашем магазине.
________________________________________________
идентификатор заказа: {id}
дата заказа: {date}
________________________________________________
all right reserved
"""


@api.route("/")
class Orders(Resource):
    @jwt_required
    @api.marshal_with(order_id, mask=None)
    @api.expect(new_order, validate=True)
    @api.doc(responses=get_codes(200), security="apiKey", params=auth)
    def post(self):
        order: Order = Order(**api.payload, login=get_jwt_identity()).commit
        recipients: List[str] = [api.payload.get("email")]
        body: str = body_template.format(
            firstName=order.firstName,
            id=order.id,
            date=date.today().strftime("%d %B %Y")
            )
        msg: Message = Message(
            "HoneyBunny заказ №{}".format(order.id),
            recipients=recipients,
            body=body
        )
        mail.send(msg)
        return order

    @jwt_required
    @api.marshal_list_with(order_model, mask=None)
    @api.doc(responses=get_codes(200), security="apiKey", params=auth)
    def get(self):
        return Order.all(get_jwt_identity())
