from typing import Tuple

from flask_admin.contrib.sqla import ModelView
from flask_login import current_user 

from app.plugin.admin.form.album_tag_form import AlbumTagForm


class AlbumTagAdminView(ModelView):
    form: AlbumTagForm = AlbumTagForm
    column_list: Tuple[str, ...] = ('id', 'album.name', 'tag.name')
    column_searchable_list: Tuple[str, ...] = ('id', 'album.name', 'tag.name')

    def is_accessible(self) -> bool:
        return current_user.is_authenticated
