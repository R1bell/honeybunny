from flask import Blueprint
from flask_restplus import Api

from app.api.auth.namespace import AUTH_NAMESPACE
from app.api.busket.namespace import BUSKET_NAMESPACE
from app.api.category.namespace import CATEGORY_NAMESPACE
from app.api.good.namespace import GOOD_NAMESPACE
from app.api.order.namespace import ORDER_NAMESPACE


def create_api() -> Blueprint:
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(blueprint, title='honey-bunny')
    api.add_namespace(GOOD_NAMESPACE)
    api.add_namespace(AUTH_NAMESPACE)
    api.add_namespace(CATEGORY_NAMESPACE)
    api.add_namespace(BUSKET_NAMESPACE)
    api.add_namespace(ORDER_NAMESPACE)
    return blueprint
