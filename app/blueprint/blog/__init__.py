from flask import Blueprint

from app.blueprint.blog.view.album_detail_view import AlbumDetailView
from app.blueprint.blog.view.home_view import HomeView


bp: Blueprint = Blueprint(name='blog', import_name=__name__, url_prefix='/')
bp.add_url_rule(rule='/', view_func=HomeView.as_view(name='home'))
bp.add_url_rule(rule='/albums/<string:slug>', view_func=AlbumDetailView.as_view(name='album_detail'))
