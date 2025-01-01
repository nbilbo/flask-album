from typing import Any
from typing import Dict

from flask_restful import fields, marshal
from flask_restful import Resource


resource_fields = {
    'albums': fields.Url(endpoint='api.album_list', absolute=True),
    'tags': fields.Url(endpoint='api.tag_list', absolute=True),
}

class HomeResource(Resource):
    @staticmethod
    def get() -> Dict[Any, Any]:
        return marshal(data={}, fields=resource_fields)
