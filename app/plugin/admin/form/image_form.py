from flask_admin.form import BaseForm
from wtforms.fields import FileField
from wtforms.fields import StringField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

from app.util.query import enabled_albums


class ImageForm(BaseForm):
    source: FileField = FileField(label='Image', validators=[DataRequired()])
    album: QuerySelectField = QuerySelectField(label='Album', validators=[DataRequired()], query_factory=enabled_albums)
