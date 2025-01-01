import traceback
from typing import Any
from typing import Dict
from typing import Optional

import cloudinary
import cloudinary.uploader
from werkzeug.datastructures import FileStorage

from app.plugin.database import db
from app.model.album_model import AlbumModel


class CreateAlbumController:
    def insert(self, fields: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self._check_fields(fields)
            album: AlbumModel = self._insert_album(fields)

        except Exception as error:
            traceback.print_exc()
            return {'success': False, 'error': str(error)}

        else:
            message = 'Record was successfully created.'
            return {'success': True, 'message': message, 'model': album}

    @staticmethod
    def _check_fields(fields: Dict[Any, Any]) -> None:
        name: Optional[str] = fields.get('name', None)
        slug: Optional[str] = fields.get('slug', None)
        about: Optional[str] = fields.get('about', None)
        thumbnail: Optional[FileStorage] = fields.get('thumbnail', None)

        cloudinary_name: Optional[str] = fields.get('cloudinary_name', None)
        cloudinary_key: Optional[str] = fields.get('cloudinary_key', None)
        cloudinary_secret: Optional[str] = fields.get('cloudinary_secret', None)
        cloudinary_folder: Optional[str] = fields.get('cloudinary_folder', None)

        if name is None:
            raise Exception('name can\'t be None')

        if slug is None:
            raise Exception('slug can\'t be None')

        if about is None:
            raise Exception('about can\'t be None')

        if thumbnail is None:
            raise Exception('thumbnail can\'t be None')

        if not len(name):
            raise Exception('name can\'t be blank')

        if not len(thumbnail.filename):
            raise Exception('thumbnail can\'t be blank')

        if cloudinary_name is None:
            raise Exception('cloudinary_name can\'t be None')

        if cloudinary_key is None:
            raise Exception('cloudinary_key can\'t be None')

        if cloudinary_secret is None:
            raise Exception('cloudinary_secret can\'t be None')

        if cloudinary_folder is None:
            raise Exception('cloudinary_folder can\'t be None')

    @staticmethod
    def _insert_album(fields: Dict[Any, Any]) -> AlbumModel:
        name: str = fields.get('name')
        slug: str = fields.get('slug')
        about: str = fields.get('about')
        thumbnail: FileStorage = fields.get('thumbnail')

        cloudinary_name: str = fields.get('cloudinary_name')
        cloudinary_key: str = fields.get('cloudinary_key')
        cloudinary_secret: str = fields.get('cloudinary_secret')
        cloudinary_folder: str = fields.get('cloudinary_folder')
        cloudinary.config(cloud_name=cloudinary_name, api_key=cloudinary_key, api_secret=cloudinary_secret)

        upload_result: Any = cloudinary.uploader.upload(thumbnail, folder=cloudinary_folder)
        public_id: str = upload_result.get('public_id')
        secure_url: str = upload_result.get('secure_url')

        album: AlbumModel = AlbumModel(name=name, slug=slug, about=about, thumbnail=secure_url, public_id=public_id)
        db.session.add(album)
        db.session.commit()

        return album
