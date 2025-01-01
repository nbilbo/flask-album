import traceback
from typing import Any
from typing import Dict
from typing import Optional

import cloudinary
import cloudinary.uploader

from app.model.image_model import ImageModel
from app.plugin.database import db


class DeleteImageController:
    def delete(self, fields: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self._check_fields(fields)
            self._delete_image(fields)

        except Exception as error:
            traceback.print_exc()
            return {'success': False, 'error': str(error)}
        
        else:
            message = ' Record was successfully deleted.'
            return {'success': True, 'message': message}

    @staticmethod
    def _check_fields(fields: Dict[Any, Any]) -> None:
        id_: Optional[int] = fields.get('id', None)
        cloudinary_name: Optional[str] = fields.get('cloudinary_name', None)
        cloudinary_key: Optional[str] = fields.get('cloudinary_key', None)
        cloudinary_secret: Optional[str] = fields.get('cloudinary_secret', None)

        if id_ is None:
            raise Exception('id can\'t be None')

        if cloudinary_name is None:
            raise Exception('cloudinary_name can\'t be None')

        if cloudinary_key is None:
            raise Exception('cloudinary_key can\'t be None')

        if cloudinary_secret is None:
            raise Exception('cloudinary_secret can\'t be None')

    @staticmethod
    def _delete_image(fields: Dict[Any, Any]) -> None:
        id_: int = fields.get('id')
        image: Optional[ImageModel] = db.session.execute(db.select(ImageModel).where(ImageModel.id == id_)).scalar()

        cloudinary_name: str = fields.get('cloudinary_name')
        cloudinary_key: str = fields.get('cloudinary_key')
        cloudinary_secret: str = fields.get('cloudinary_secret')
        cloudinary.config(cloud_name=cloudinary_name, api_key=cloudinary_key, api_secret=cloudinary_secret)

        if image is None:
            raise Exception('Image not found.')

        cloudinary.uploader.destroy(public_id=image.public_id)
        db.session.delete(image)
        db.session.commit()
