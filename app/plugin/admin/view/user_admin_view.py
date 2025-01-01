from typing import Tuple

from flask_admin.contrib.sqla import ModelView
from flask_login import current_user 


class UserAdminView(ModelView):
    can_create: bool = False
    can_edit: bool = False
    can_delete: bool = True
    column_list: Tuple[str] = ('name', 'username', 'password')

    def is_accessible(self) -> bool:
        return current_user.is_authenticated
