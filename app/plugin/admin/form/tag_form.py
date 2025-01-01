from flask_admin.form import BaseForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class TagForm(BaseForm):
    name: StringField = StringField(label='Name', validators=[DataRequired()])
