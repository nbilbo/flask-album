from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.plugin.database import db

if TYPE_CHECKING:
    from app.model.album_model import AlbumModel
    from app.model.tag_model import TagModel


class AlbumTagModel(db.Model):
    __tablename__ = 'album_tag'

    id: Mapped[int] = mapped_column(primary_key=True)
    album_id: Mapped[int] = mapped_column(ForeignKey('album.id'))
    tag_id: Mapped[int] = mapped_column(ForeignKey('tag.id'))

    album: Mapped['AlbumModel'] = relationship(back_populates='album_tag')
    tag: Mapped['TagModel'] = relationship(back_populates='album_tag')
