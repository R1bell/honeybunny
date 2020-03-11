from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import GOOD_NAMESPACE as api

good_model: Model = api.model("new good", {
    "name": fields.String(required=True),
    "weight": fields.String(required=True),
    "description": fields.String(required=True),
    "measure": fields.String(required=True),
    "price": fields.Integer(required=True),
    "category": fields.String(required=True),
    "link": fields.String(required=True)
})

good_with_id: Model = api.inherit("good", good_model, {
    "id": fields.Integer()
})
