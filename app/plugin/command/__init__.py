from typing import Optional

from flask import Flask
from flask import current_app

from app.model.album_model import AlbumModel
from app.model.album_tag_model import AlbumTagModel
from app.model.image_model import ImageModel
from app.model.tag_model import TagModel
from app.model.user_model import UserModel
from app.plugin.database import db
from app.util.security import get_password_hash


def init_user_admin(app: Flask) -> None:
    with app.app_context():
        name: Optional[str] = current_app.config['ADMIN_NAME']
        username: Optional[str] = current_app.config['ADMIN_USERNAME']
        password: Optional[str] = current_app.config['ADMIN_PASSWORD']
        
        if all((name, username, password)):
            if db.session.execute(db.select(UserModel).where(UserModel.username == username)).scalar() is None:
                hashed_password: bytes = get_password_hash(password)
                db.session.add(UserModel(name=name, username=username, password=hashed_password))
                db.session.commit()


def init_database(app: Flask) -> None:
    with app.app_context():
        db.create_all()


def init_app(app: Flask) -> None:
    """Call commands when server is started."""
    init_database(app)
    init_user_admin(app)
