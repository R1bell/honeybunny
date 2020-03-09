from flask_restplus import fields

from flask_restplus.model import Model
from app.api.auth.namespace import AUTH_NAMESPACE as api

login_model: Model = api.model("login", {
    "login": fields.String(required=True),
    "password": fields.String(required=True)
})

registration_model: Model = api.inherit("registration", login_model, {
    "firstName": fields.String(required=True),
    "lastName": fields.String(required=True),
    "email": fields.String(required=True)
})

auth_response_model: Model = api.model("auth response", {
    "accessToken": fields.String(),
    "id": fields.Integer(),
    "firstName": fields.String(),
    "lastName": fields.String()
})

user_model: Model = api.model("user", {
    "id": fields.Integer(),
    "firstName": fields.String(),
    "lastName": fields.String(),
    "login": fields.String(),
    "email": fields.String()
})

login_response_model: Model = api.model("login response", {
    "accessToken": fields.String(),
    "user": fields.Nested(user_model)
})
