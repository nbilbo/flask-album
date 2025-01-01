from typing import Any
from typing import Dict
from typing import List

from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal

from app.model.tag_model import TagModel


resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class TagListResource(Resource):
    @staticmethod
    def get() -> List[Dict[Any, Any]]:
        tags: List[TagModel] = TagModel.query.all()

        return marshal(data=tags, fields=resource_fields)
