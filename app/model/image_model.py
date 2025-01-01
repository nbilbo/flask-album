from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.plugin.database import db

if TYPE_CHECKING:
    from app.model.album_model import AlbumModel


class ImageModel(db.Model):
    __tablename__ = 'image'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(nullable=False)
    public_id: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    updated: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now, onupdate=datetime.now)

    # image have one album.
    album_id: Mapped[int] = mapped_column(ForeignKey('album.id'))
    album: Mapped['AlbumModel'] = relationship(back_populates='images')
