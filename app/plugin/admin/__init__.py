from flask import Flask
from flask_admin import Admin

from app.model.album_model import AlbumModel
from app.model.album_tag_model import AlbumTagModel
from app.model.image_model import ImageModel
from app.model.tag_model import TagModel
from app.model.user_model import UserModel
from app.plugin.admin.view.album_admin_view import AlbumAdminView
from app.plugin.admin.view.album_tag_admin_view import AlbumTagAdminView
from app.plugin.admin.view.image_admin_view import ImageAdminView
from app.plugin.admin.view.index_view import IndexView
from app.plugin.admin.view.tag_admin_view import TagAdminView
from app.plugin.admin.view.user_admin_view import UserAdminView
from app.plugin.database import db


def init_app(app: Flask) -> None:
    """Add an admin manager page."""
    admin = Admin(app, name=app.config['APP_NAME'], index_view=IndexView(), endpoint='admin')
    admin.add_view(UserAdminView(model=UserModel, session=db.session, name='Users'))
    admin.add_view(AlbumAdminView(model=AlbumModel, session=db.session, name='Albums'))
    admin.add_view(ImageAdminView(model=ImageModel, session=db.session, name='Images'))
    admin.add_view(TagAdminView(model=TagModel, session=db.session, name='Tags'))
    admin.add_view(AlbumTagAdminView(model=AlbumTagModel, session=db.session, name='Album Tags'))
