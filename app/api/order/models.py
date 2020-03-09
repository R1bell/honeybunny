from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import ORDER_NAMESPACE as api

order_model: Model = api.model("order", {
    "wayOfPaiment": fields.String(required=True),
    "oddMoney": fields.String(required=True),
    "address": fields.String(required=True),
    "porch": fields.String(),
    "floor": fields.String(),
    "apartment": fields.String(),
    "comment": fields.String(),
    "firstName": fields.String(required=True),
    "lastName": fields.String(required=True),
    "phone": fields.String(required=True),
    "email": fields.String()
})

order_id: Model = api.model("order id", {
    "id": fields.Integer
})
