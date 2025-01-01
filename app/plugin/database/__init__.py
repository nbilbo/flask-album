from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db: SQLAlchemy = SQLAlchemy(model_class=Base)

def init_app(app: Flask) -> None:
    """Configure database."""
    db.init_app(app)
