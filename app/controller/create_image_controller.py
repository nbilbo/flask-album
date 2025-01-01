import traceback
from typing import Any
from typing import Dict
from typing import Optional

import cloudinary
import cloudinary.uploader
from werkzeug.datastructures import FileStorage

from app.model.album_model import AlbumModel
from app.model.image_model import ImageModel
from app.plugin.database import db


class CreateImageController:
    def insert(self, fields: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self._check_fields(fields)
            image: ImageModel = self._insert_image(fields)

        except Exception as error:
            traceback.print_exc()
            return {'success': False, 'error': str(error)}
        
        else:
            message = 'Record was successfully created.'
            return {'success': True, 'message': message, 'model': image}


    @staticmethod
    def _check_fields(fields: Dict[Any, Any]) -> None:
        source: Optional[FileStorage] = fields.get('source', None)
        album: Optional[AlbumModel] = fields.get('album', None)

        cloudinary_name: Optional[str] = fields.get('cloudinary_name', None)
        cloudinary_key: Optional[str] = fields.get('cloudinary_key', None)
        cloudinary_secret: Optional[str] = fields.get('cloudinary_secret', None)
        cloudinary_folder: Optional[str] = fields.get('cloudinary_folder', None)

        if source is None:
            raise Exception('source can\'t be None.')

        if not len(source.filename):
            raise Exception('source can\'t be blank.')
        
        if album is None:
            raise Exception('album can\'t be None.')

        if cloudinary_name is None:
            raise Exception('cloudinary_name can\'t be None.')

        if cloudinary_key is None:
            raise Exception('cloudinary_key can\'t be None.')

        if cloudinary_secret is None:
            raise Exception('cloudinary_secret can\'t be None.')

        if cloudinary_folder is None:
            raise Exception('cloudinary_folder can\'t be None.')

    @staticmethod
    def _insert_image(fields: Dict[Any, Any]) -> ImageModel:
        album: AlbumModel = fields.get('album')
        source: FileStorage = fields.get('source')

        cloudinary_name: str = fields.get('cloudinary_name')
        cloudinary_key: str = fields.get('cloudinary_key')
        cloudinary_secret: str = fields.get('cloudinary_secret')
        cloudinary_folder: str = fields.get('cloudinary_folder')
        cloudinary.config(cloud_name=cloudinary_name, api_key=cloudinary_key, api_secret=cloudinary_secret)

        upload_result: Any = cloudinary.uploader.upload(source, folder=cloudinary_folder)
        public_id: str = upload_result.get('public_id')
        secure_url: str = upload_result.get('secure_url')

        image = ImageModel(album=album, source=secure_url, public_id=public_id)
        db.session.add(image)
        db.session.execute(db.update(AlbumModel).where(AlbumModel.id == album.id))
        db.session.commit()

        return image
