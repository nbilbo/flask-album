from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.plugin.database import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)

    def __str__(self) -> str:
        return str(self.username)
