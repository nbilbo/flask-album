from typing import Any
from typing import Dict
from typing import Optional

from flask import abort
from flask_restful import fields
from flask_restful import marshal
from flask_restful import Resource

from app.model.album_model import AlbumModel


images_fields = {
    'id': fields.Integer,
    'source': fields.String(attribute='source'),
}

album_tag_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='tag.name')
}

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'slug': fields.String,
    'about': fields.String,
    'updated': fields.DateTime,
    'created': fields.DateTime,
    'thumbnail': fields.String,
    'images': fields.List(fields.Nested(images_fields)),
    'tags': fields.List(fields.Nested(album_tag_fields), attribute='album_tag')
}

class AlbumDetailResource(Resource):
    @staticmethod
    def get(slug: str) -> Dict[Any, Any]:
        album: Optional[AlbumModel] = AlbumModel.query.filter(AlbumModel.slug == slug).scalar()
        if album is None: abort(404)

        return  marshal(data=album, fields=resource_fields)
