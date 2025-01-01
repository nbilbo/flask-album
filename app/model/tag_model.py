from typing import List
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.plugin.database import db

if TYPE_CHECKING:
    from app.model.album_tag_model import AlbumTagModel


class TagModel(db.Model):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    # the same tag can be used by many albums and posts.
    album_tag: Mapped[List['AlbumTagModel']] = relationship(back_populates='tag')

    def __str__(self) -> str:
        return str(self.name)
