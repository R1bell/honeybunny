from flask_restplus import Namespace

authorization = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "**'Bearer JWT'**, where JWT is the token"
    }
}
BUSKET_NAMESPACE: Namespace = Namespace(
    "busket",
    path="/busket",
    authorizations=authorization
)
