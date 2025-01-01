from flask import Flask
from app.blueprint import auth
from app.blueprint import blog
from app.blueprint import error
from app.plugin import admin
from app.plugin import api_rest_full
from app.plugin import command
from app.plugin import cors
from app.plugin import database
from app.plugin import login_manager
from app.settings import Settings


def create_app() -> Flask:
    app = Flask(import_name=__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Settings())

    database.init_app(app)
    command.init_app(app)
    api_rest_full.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)

    app.register_blueprint(blueprint=blog.bp)
    app.register_blueprint(blueprint=auth.bp)
    app.register_blueprint(blueprint=error.bp)

    return app
