from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import BUSKET_NAMESPACE as api

item_amount: Model = api.model("amount", {
    "amount": fields.Integer(required=True)
})

item_model: Model = api.inherit("item", item_amount, {
    "user_id": fields.Integer(required=True),
    "good_id": fields.Integer(required=True)
})

good_model: Model = api.model("good", {
    "id": fields.Integer,
    "name": fields.String,
    "weight": fields.String,
    "description": fields.String,
    "measure": fields.String,
    "price": fields.Float,
    "category": fields.String
})

item_with_good = api.inherit("item with good", item_amount, {
    "id": fields.Integer(),
    "good": fields.Nested(good_model)
})
