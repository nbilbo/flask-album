from flask import Blueprint

from app.blueprint.auth.view.login_view import LoginView
from app.blueprint.auth.view.logout_view import LogoutView


bp: Blueprint = Blueprint(name='auth', import_name=__name__, url_prefix='/auth')
bp.add_url_rule(rule='/login', view_func=LoginView.as_view(name='login'))
bp.add_url_rule(rule='/logout', view_func=LogoutView.as_view(name='logout'))
