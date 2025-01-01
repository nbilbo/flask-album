from flask_admin.form import BaseForm
from wtforms.fields import FileField
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class AlbumForm(BaseForm):
    thumbnail: FileField = FileField(label='Thumbnail', validators=[DataRequired()])
    name: StringField = StringField(label='Name', validators=[DataRequired()])
    slug: StringField = StringField(label='Slug', validators=[DataRequired()])
    about: StringField = StringField(label='About', validators=[DataRequired()])
