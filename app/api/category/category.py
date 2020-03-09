from flask_restplus import Resource

from app.api.category.models import category_model, category_with_id
from app.api.category.namespace import CATEGORY_NAMESPACE as api
from app.api.responses import get_codes
from app.models.category import Category


@api.route("/")
class Categories(Resource):
    @api.expect(category_model, validate=True)
    @api.doc(responses=get_codes(200, 409))
    def post(self):
        if Category(**api.payload).commit():
            return "success"
        api.abort(409)

    @api.marshal_list_with(category_with_id, mask=None)
    @api.doc(responses=get_codes(200))
    def get(self):
        return Category.all()


@api.route("/<id>")
@api.doc(params={"id": "id"})
class CategoriesById(Resource):
    @api.doc(responses=get_codes(200, 404))
    def delete(self, id: int):
        return "success" if Category.delete(id=id) else api.abort(404)

    @api.marshal_with(category_with_id, mask=None)
    @api.doc(responses=get_codes(200, 404))
    def get(self, id: int):
        category: Category = Category.first(id=id)
        return category if category else api.abort(404)
