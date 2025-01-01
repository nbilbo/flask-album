from flask import Flask
from flask_restful import Api


from app.plugin.api_rest_full.resource.album_detail_resource import AlbumDetailResource
from app.plugin.api_rest_full.resource.album_list_resource import AlbumListResource
from app.plugin.api_rest_full.resource.home_resource import HomeResource
from app.plugin.api_rest_full.resource.tag_list_resource import TagListResource


def init_app(app: Flask) -> None:
    """Add endpoints to send json data."""
    api: Api = Api(app, prefix='/api')

    api.add_resource(HomeResource, '/', endpoint='api.home')
    api.add_resource(AlbumListResource, '/albums', endpoint='api.album_list')
    api.add_resource(TagListResource, '/tags', endpoint='api.tag_list')
    api.add_resource(AlbumDetailResource, '/albums/<string:slug>', endpoint='api.album_detail')
