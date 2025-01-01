from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import Response
from flask import url_for
from flask.views import MethodView
from flask_sqlalchemy.query import QueryPagination

from app.model.album_model import AlbumModel
from app.model.image_model import ImageModel


class AlbumDetailView(MethodView):
    @staticmethod
    def get(slug: str) -> Union[str, Response]:
        page: int = request.args.get(key='page', default=1, type=int)
        images_per_page_count:int = current_app.config.get('IMAGES_PER_PAGE_COUNT', 4)
        album: Optional[AlbumModel] = AlbumModel.query.filter(AlbumModel.slug == slug).scalar()

        if album is None: 
            return redirect(location=url_for(endpoint='blog.home'))

        pagination: QueryPagination = ImageModel.query.filter(ImageModel.album == album).order_by(ImageModel.created.desc()).paginate(page=page, per_page=images_per_page_count)
        images: List[ImageModel] = pagination.items
        context: Dict[str, Union[AlbumModel, QueryPagination, List[ImageModel]]] = {'album': album, 'pagination': pagination, 'images': images}

        return render_template(template_name_or_list='blog/album_detail.html', **context)
