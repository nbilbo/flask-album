from datetime import datetime
from typing import List
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.plugin.database import db

if TYPE_CHECKING:
    from app.model.album_tag_model import AlbumTagModel
    from app.model.image_model import ImageModel


class AlbumModel(db.Model):
    __tablename__ = 'album'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)
    about: Mapped[str] = mapped_column(nullable=False)
    thumbnail: Mapped[str] = mapped_column(nullable=False)
    public_id: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    updated: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now, onupdate=datetime.now)

    # album have many images.
    images: Mapped[List['ImageModel']] = relationship(back_populates='album')

    # album have many tags.
    album_tag: Mapped[List['AlbumTagModel']] = relationship(back_populates='album')

    def __str__(self) -> str:
        return str(self.name)
