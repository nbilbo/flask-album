from typing import List

from app.model.album_model import AlbumModel
from app.model.tag_model import TagModel
from app.model.user_model import UserModel


def enabled_users() -> List[UserModel]:
    return UserModel.query.all()


def enabled_albums() -> List[AlbumModel]:
    return AlbumModel.query.order_by(AlbumModel.created).all()


def enabled_tags() -> List[TagModel]:
    return TagModel.query.all()
