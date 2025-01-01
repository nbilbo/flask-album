from flask_admin.form import BaseForm
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

from app.util.query import enabled_albums
from app.util.query import enabled_tags


class AlbumTagForm(BaseForm):
    album: QuerySelectField = QuerySelectField(label='Album', validators=[DataRequired()], query_factory=enabled_albums)
    tag: QuerySelectField = QuerySelectField(label='Tag', validators=[DataRequired()], query_factory=enabled_tags)
