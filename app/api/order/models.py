from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import ORDER_NAMESPACE as api

new_order: Model = api.model("new order", {
    "wayOfPaiment": fields.String(required=True),
    "oddMoney": fields.String(),
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

order_model = api.inherit("order", order_id, {
    "wayOfPaiment": fields.String(),
    "oddMoney": fields.String(),
    "address": fields.String(),
    "porch": fields.String(),
    "floor": fields.String(),
    "apartment": fields.String(),
    "comment": fields.String(),
    "firstName": fields.String(),
    "lastName": fields.String(),
    "phone": fields.String(),
    "email": fields.String()
})
