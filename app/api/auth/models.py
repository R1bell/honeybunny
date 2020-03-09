from flask_restplus import fields

from flask_restplus.model import Model
from app.api.auth.namespace import AUTH_NAMESPACE as api

registration_model: Model = api.model("registration", {
    "firstName": fields.String(required=True),
    "lastName": fields.String(required=True),
    "login": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

login_model: Model = api.model("login", {
    "login": fields.String(required=True),
    "password": fields.String(required=True)
})

auth_response_model: Model = api.model("auth response", {
    "accessToken": fields.String(),
    "userId": fields.Integer(),
    "firstName": fields.String(),
    "lastName": fields.String()
})
