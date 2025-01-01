from typing import Any
from typing import Optional

from flask import Flask
from flask_login import LoginManager

from app.model.user_model import UserModel
from app.plugin.database import db
from app.schema.user_public_schema import UserPublicSchema


login_manager: LoginManager = LoginManager()

@login_manager.user_loader
def user_loader(username: Optional[str]) -> Optional[UserPublicSchema]:
    user: Optional[UserModel] = db.session.execute(db.select(UserModel).where(UserModel.username == username)).scalar()

    if user is None:
        return None
    
    else:
        user_public: UserPublicSchema = UserPublicSchema()
        user_public.id = username
        return user_public


@login_manager.request_loader
def request_loader(request: Any) -> Optional[UserPublicSchema]:
    username: Optional[str] = request.form.get('username')

    if username is None:
        return None

    else:
        user_public: UserPublicSchema = UserPublicSchema()
        user_public.id = username
        return user_public


def init_app(app: Flask) -> None:
    """Configure login/logout."""
    login_manager.init_app(app)
