from typing import Dict
from typing import List

from flask import render_template
from flask.views import MethodView

from app.model.album_model import AlbumModel


class HomeView(MethodView):
    @staticmethod
    def get() -> str:
        albums: List[AlbumModel] = AlbumModel.query.order_by(AlbumModel.updated.desc()).all()
        context: Dict[str, List[AlbumModel]] = {'albums': albums}

        return render_template(template_name_or_list='blog/home.html', **context)
