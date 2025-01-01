from flask import flash
from flask import redirect
from flask import Response
from flask import url_for
from flask.views import MethodView
from flask_login import logout_user


class LogoutView(MethodView):
    @staticmethod
    def get() -> Response:
        logout_user()
        flash(message='Logged out.', category='success')

        return redirect(location=url_for(endpoint='blog.home'))
