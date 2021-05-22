from flask import Flask, current_app
# logging
import logging
from logging.handlers import RotatingFileHandler
# configuration
from config import Config

# international
from flask_babel import Babel, lazy_gettext as _l
from babel import negotiate_locale
from flask import request
babel = Babel()
from flask_babel_js import BabelJS
babel_js = BabelJS()
# DB
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# DB migration
from flask_migrate import Migrate
migrate = Migrate()
# login Manager
from flask_login import LoginManager
login = LoginManager()
login.login_message = _l('Please login to access this page.')

import os

def create_app(config_class=Config):
    # ini app
    app = Flask(__name__)
    # db
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    migrate.init_app(app, db)
    # login
    login.init_app(app)
    # babel
    babel.init_app(app)
    babel_js.init_app(app)
    # add config
    app.config.from_object(config_class)
    app.app_context().push()

    # the main of the app
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # editor
    from app.editor import bp as editor_bp
    app.register_blueprint(editor_bp)

    # logs
    if not os.path.exists('logs'):
        os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/oauth.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask example startup')

    return app

# international
@babel.localeselector
def get_locale():
    preferred = [x.replace('-', '_') for x in request.accept_languages.values()]
    return negotiate_locale(preferred, current_app.config['LANGUAGES'])

from app import models_editor
