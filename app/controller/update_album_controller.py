import traceback
from typing import Any, Optional
from typing import Dict

import cloudinary
import cloudinary.uploader
from werkzeug.datastructures import FileStorage

from app.model.album_model import AlbumModel
from app.plugin.database import db


class UpdateAlbumController:
    def edit(self, fields: Dict[Any, Any]) -> Dict:
        try:
            self._check_fields(fields)
            album: AlbumModel = self._update_album(fields)
        
        except Exception as error:
            traceback.print_exc()
            return {'success': False, 'error': str(error)}

        else:
            message = 'Record was successfully saved.'
            return {'success': True, 'message': message, 'model': album}

    @staticmethod
    def _check_fields(fields: Dict[Any, Any]) -> None:
        id_: Optional[int] = fields.get('id', None)
        name: Optional[str] = fields.get('name', None)
        slug: Optional[str] = fields.get('slug', None)
        about: Optional[str] = fields.get('about', None)
        thumbnail: Optional[FileStorage] = fields.get('thumbnail', None)

        cloudinary_name: Optional[str] = fields.get('cloudinary_name', None)
        cloudinary_key: Optional[str] = fields.get('cloudinary_key', None)
        cloudinary_secret: Optional[str] = fields.get('cloudinary_secret', None)
        cloudinary_folder: Optional[str] = fields.get('cloudinary_folder', None)

        if id_ is None:
            raise Exception('id can\'t be None.')

        if name is None:
            raise Exception('name can\'t be None.')

        if slug is None:
            raise Exception('slug can\'t be None.')

        if about is None:
            raise Exception('about can\'t be None.')

        if thumbnail is None:
            raise Exception('thumbnail can\'t be None.')

        if not len(thumbnail.filename):
            raise Exception('thumbnail can\'t be blank.')

        if cloudinary_name is None:
            raise Exception('cloudinary_name can\'t be None.')

        if cloudinary_key is None:
            raise Exception('cloudinary_key can\'t be None.')

        if cloudinary_secret is None:
            raise Exception('cloudinary_secret can\'t be None.')

        if cloudinary_folder is None:
            raise Exception('cloudinary_folder can\'t be None.')

    @staticmethod
    def _update_album(fields: Dict[Any, Any]) -> AlbumModel:
        id_: int = fields.get('id')
        album: Optional[AlbumModel] = db.session.execute(db.select(AlbumModel).where(AlbumModel.id == id_)).scalar()

        name: str = fields.get('name')
        slug: str = fields.get('slug')
        about: str = fields.get('about')
        thumbnail: FileStorage = fields.get('thumbnail')

        cloudinary_name: str = fields.get('cloudinary_name')
        cloudinary_key: str = fields.get('cloudinary_key')
        cloudinary_secret: str = fields.get('cloudinary_secret')
        cloudinary_folder: str = fields.get('cloudinary_folder')
        cloudinary.config(cloud_name=cloudinary_name, api_key=cloudinary_key, api_secret=cloudinary_secret)

        if album is None:
            raise Exception('Album not found.')

        cloudinary.uploader.destroy(public_id=album.public_id)
        upload_result: Any = cloudinary.uploader.upload(thumbnail, folder=cloudinary_folder)
        public_id: str = upload_result.get('public_id')
        secure_url: str = upload_result.get('secure_url')

        album.public_id = public_id
        album.thumbnail = secure_url
        album.name = name
        album.slug = slug
        album.about = about
        db.session.commit()

        return album
