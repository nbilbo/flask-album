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

from app.controller.create_image_controller import CreateImageController
from app.controller.delete_image_controller import DeleteImageController
from app.controller.update_image_controller import UpdateImageController
from app.model.album_model import AlbumModel
from app.model.image_model import ImageModel
from app.plugin.admin.form.image_form import ImageForm


class ImageAdminView(ModelView):
    form: ImageForm = ImageForm
    column_list: Tuple[str, ...] = ('id', 'album', 'source')
    column_searchable_list: Tuple[str, ...] = ('id', 'album.name')

    def is_accessible(self) -> bool:
        return current_user.is_authenticated

    def create_model(self, form: ImageForm) -> Optional[ImageModel]:
        source: Optional[FileStorage] = form.data.get('source', None)
        album: Optional[AlbumModel] = form.data.get('album', None)

        cloudinary_name: Optional[str] = current_app.config['CLOUDINARY_NAME']
        cloudinary_key: Optional[str] = current_app.config['CLOUDINARY_KEY']
        cloudinary_secret: Optional[str] = current_app.config['CLOUDINARY_SECRET']
        cloudinary_folder: Optional[str] = current_app.config['CLOUDINARY_FOLDER']

        fields: Dict[str, Union[str, AlbumModel, FileStorage, None]] = {
            'source': source, 
            'album': album, 
            'cloudinary_name': cloudinary_name,
            'cloudinary_key': cloudinary_key,
            'cloudinary_secret': cloudinary_secret,
            'cloudinary_folder': cloudinary_folder
        }

        controller: CreateImageController = CreateImageController()
        response: Dict[Any, Any] = controller.insert(fields)

        if response['success']:
            return response['model']

        else:
            flash(message=response['error'], category='error')
            return None

    def update_model(self, form: ImageForm, model: ImageModel) -> bool:
        source: Optional[FileStorage] = form.data.get('source', None)
        album: Optional[AlbumModel] = form.data.get('album', None)

        cloudinary_name: Optional[str] = current_app.config['CLOUDINARY_NAME']
        cloudinary_key: Optional[str] = current_app.config['CLOUDINARY_KEY']
        cloudinary_secret: Optional[str] = current_app.config['CLOUDINARY_SECRET']
        cloudinary_folder: Optional[str] = current_app.config['CLOUDINARY_FOLDER']


        fields: Dict[str, Union[str, int, AlbumModel, FileStorage, None]] = {
            'id': model.id,
            'source': source,
            'album': album,
            'cloudinary_name': cloudinary_name,
            'cloudinary_key': cloudinary_key,
            'cloudinary_secret': cloudinary_secret,
            'cloudinary_folder': cloudinary_folder
        }

        controller: UpdateImageController = UpdateImageController()
        response: Dict[Any, Any] = controller.update(fields)

        if response['success']:
            return True

        else:
            flash(message=response['error'], category='error')
            return False

    def delete_model(self, model: ImageModel) -> bool:
        cloudinary_name: Optional[str] = current_app.config['CLOUDINARY_NAME']
        cloudinary_key: Optional[str] = current_app.config['CLOUDINARY_KEY']
        cloudinary_secret: Optional[str] = current_app.config['CLOUDINARY_SECRET']
        
        fields: Dict[str, Union[int, str, None]] = {
            'id': model.id,
            'cloudinary_name': cloudinary_name,
            'cloudinary_key': cloudinary_key,
            'cloudinary_secret': cloudinary_secret
        }

        controller: DeleteImageController = DeleteImageController()
        response: Dict[Any, Any] = controller.delete(fields)

        if response['success']:
            return True

        else:
            flash(message=response['error'], category='error')
            return False
