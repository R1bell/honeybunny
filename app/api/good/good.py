from typing import List, Optional

from flask_restplus import Resource

from app.api.good.models import good_with_id, good_model
from app.api.good.namespace import GOOD_NAMESPACE as api
from app.api.responses import get_codes
from app.models.good import Good
from app.models.category import Category


@api.route("/")
class Goods(Resource):
    @api.marshal_list_with(good_with_id, mask=None)
    @api.doc(responses=get_codes(200))
    def get(self):
        return Good.all()

    @api.expect(good_model, validate=True)
    @api.doc(responses=get_codes(200, 404, 409))
    def post(self):
        category_name = api.payload.pop("category")
        category = Category.first(name=category_name)
        if not category:
            api.abort(404, "Category doesn't exist")

        good: Good = Good(category=category, **api.payload)
        return "success" if good.commit() else api.abort(409)


@api.route("/<category>")
class GoodsByCategory(Resource):
    @api.marshal_list_with(good_with_id, mask=None)
    @api.doc(responses=get_codes(200))
    def get(self, category: str):
        return Category.get_all_goods(category)


@api.route("/<id>")
@api.doc(params={"id": "id"})
class GoodsById(Resource):
    @api.doc(responses=get_codes(200, 404))
    def delete(self, id: int):
        return "success" if Good.delete(id=id) else api.abort(404)

    @api.expect(good_model)
    @api.doc(params={"id": "id"}, responses=get_codes(200, 404))
    def put(self, id: int):
        good: Optional[Good] = Good.first(id=id)
        good.update(**api.payload) if good else api.abort(404)
        return "success"

    @api.marshal_with(good_with_id, mask=None)
    @api.doc(responses=get_codes(200, 404))
    def get(self, id: int):
        good: Optional[Good] = Good.first(id=id)
        return good if good else api.abort(404)
