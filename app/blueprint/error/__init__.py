# https://youtu.be/uVNfQDohYNI

from typing import Dict

from flask import Blueprint
from flask import render_template
from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import Unauthorized


bp = Blueprint(name='error', import_name=__name__)

@bp.app_errorhandler(401)
def error_401(error: Unauthorized) -> str:
    context: Dict[str, Unauthorized] = {'error': error}

    return render_template(template_name_or_list='error/error.html', **context)


@bp.app_errorhandler(403)
def error_401(error: Forbidden) -> str:
    context: Dict[str, Forbidden] = {'error': error}

    return render_template(template_name_or_list='error/error.html', **context)


@bp.app_errorhandler(404)
def error_404(error: NotFound) -> str:
    context: Dict[str, NotFound] = {'error': error}

    return render_template(template_name_or_list='error/error.html', **context)
