from typing import Optional
from typing import Union

from flask import flash
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from flask.views import MethodView
from flask_login import login_user
from werkzeug import Response

from app.model.user_model import UserModel
from app.schema.user_public_schema import UserPublicSchema
from app.util.security import verify_password


class LoginView(MethodView):
    @staticmethod
    def get() -> Union[Response, str]:
        return render_template(template_name_or_list='auth/login.html')

    @staticmethod
    def post() -> Response:
        username: str = request.form.get('username')
        password: str = request.form.get('password')
        user: Optional[UserModel] = UserModel.query.filter(UserModel.username == username).scalar()

        if user is None:
            flash(message='username or password invalid.', category='danger')
            return redirect(location=url_for(endpoint='auth.login'))

        if not verify_password(password, user.password):
            flash(message='username or password invalid.', category='danger')
            return redirect(location=url_for(endpoint='auth.login'))

        else:
            user_public: UserPublicSchema = UserPublicSchema()
            user_public.id = username
            login_user(user_public)
            flash(message=f'Welcome {username}', category='success')
            return redirect(location=url_for(endpoint='blog.home'))
