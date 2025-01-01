from typing import Any
from typing import Dict
from typing import List

from flask_restful import fields
from flask_restful import marshal
from flask_restful import Resource

from app.model.album_model import AlbumModel


album_tag_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='tag.name')
}

image_fields = {
    'id': fields.Integer,
    'source': fields.String
}

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'slug': fields.String,
    'about': fields.String,
    'updated': fields.DateTime,
    'created': fields.DateTime,
    'thumbnail': fields.String,
    'images': fields.List(fields.Nested(image_fields)),
    'tags': fields.List(fields.Nested(album_tag_fields), attribute='album_tag')
}

class AlbumListResource(Resource):
    @staticmethod
    def get() -> List[Dict[Any, Any]]:
        albums: List[AlbumModel] = AlbumModel.query.order_by(AlbumModel.updated).all()

        return marshal(data=albums, fields=resource_fields)
