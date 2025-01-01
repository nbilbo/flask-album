from typing import Tuple

from flask_admin.contrib.sqla import ModelView
from flask_login import current_user 

from app.plugin.admin.form.tag_form import TagForm


class TagAdminView(ModelView):
    form: TagForm = TagForm
    column_list: Tuple[str, ...] = ('id', 'name')
    column_searchable_list: Tuple[str, ...] = ('id', 'name')

    def is_accessible(self) -> bool:
        return current_user.is_authenticated
