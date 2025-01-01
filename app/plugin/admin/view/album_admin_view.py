from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Union

from flask import current_app
from flask import flash
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.datastructures import FileStorage

from app.plugin.admin.form.album_form import AlbumForm
from app.controller.create_album_controller import CreateAlbumController
from app.controller.delete_album_controller import DeleteAlbumController
from app.controller.update_album_controller import UpdateAlbumController
from app.model.album_model import AlbumModel


class AlbumAdminView(ModelView):
    form: AlbumForm = AlbumForm
    column_list: Tuple[str] = ('id', 'name', 'slug', 'thumbnail', 'created', 'updated')
    column_searchable_list: Tuple[str, ...] = ('name', )

    def is_accessible(self) -> bool:
        return current_user.is_authenticated

    def create_model(self, form: AlbumForm) -> Optional[AlbumModel]:
        name: Optional[str] = form.data.get('name', None)
        slug: Optional[str] = form.data.get('slug', None)
        about: Optional[str] = form.data.get('about', None)
        thumbnail: Optional[FileStorage] = form.data.get('thumbnail', None)

        cloudinary_name: Optional[str] = current_app.config['CLOUDINARY_NAME']
        cloudinary_key: Optional[str] = current_app.config['CLOUDINARY_KEY']
        cloudinary_secret: Optional[str] = current_app.config['CLOUDINARY_SECRET']
        cloudinary_folder: Optional[str] = current_app.config['CLOUDINARY_FOLDER']

        fields: Dict[str, Union[str, FileStorage, None]] = {
            'name': name, 
            'slug': slug,
            'about': about,
            'thumbnail': thumbnail, 
            'cloudinary_name': cloudinary_name,
            'cloudinary_key': cloudinary_key,
            'cloudinary_secret': cloudinary_secret,
            'cloudinary_folder': cloudinary_folder
        }

        controller: CreateAlbumController = CreateAlbumController()
        response: Dict[Any, Any] = controller.insert(fields)

        if response['success']:
            return response['model']

        else:
            flash(message=response['error'], category='error')
            return None

    def update_model(self, form: AlbumForm, model: AlbumModel) -> Optional[AlbumModel]:
        name: Optional[str] = form.data.get('name', None)
        slug: Optional[str] = form.data.get('slug', None)
        about: Optional[str] = form.data.get('about', None)
        thumbnail: Optional[FileStorage] = form.data.get('thumbnail', None)

        cloudinary_name: Optional[str] = current_app.config['CLOUDINARY_NAME']
        cloudinary_key: Optional[str] = current_app.config['CLOUDINARY_KEY']
        cloudinary_secret: Optional[str] = current_app.config['CLOUDINARY_SECRET']
        cloudinary_folder: Optional[str] = current_app.config['CLOUDINARY_FOLDER']

        fields: Dict[str, Union[str, FileStorage, None]] = {
            'id': model.id,
            'name': name,
            'slug': slug,
            'about': about,
            'thumbnail': thumbnail,
            'cloudinary_name': cloudinary_name,
            'cloudinary_key': cloudinary_key,
            'cloudinary_secret': cloudinary_secret,
            'cloudinary_folder': cloudinary_folder
        }

        controller: UpdateAlbumController = UpdateAlbumController()
        response: Dict[Any, Any] = controller.edit(fields)

        if response['success']:
            return response['model']

        else:
            flash(message=response['error'], category='error')
            return None

    def delete_model(self, model: AlbumModel) -> bool:
        cloudinary_name: Optional[str] = current_app.config['CLOUDINARY_NAME']
        cloudinary_key: Optional[str] = current_app.config['CLOUDINARY_KEY']
        cloudinary_secret: Optional[str] = current_app.config['CLOUDINARY_SECRET']

        fields: Dict[str, Union[str, int, None]] = {
            'id': model.id,
            'cloudinary_name': cloudinary_name,
            'cloudinary_key': cloudinary_key,
            'cloudinary_secret': cloudinary_secret
        }

        controller: DeleteAlbumController = DeleteAlbumController()
        response: Dict[Any, Any] = controller.delete(fields)

        if response['success']:
            return True

        else:
            flash(message=response['error'], category='error')
            return False
