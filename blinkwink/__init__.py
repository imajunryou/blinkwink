from flask import Flask
from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config.from_envvar("BLINKWINK_CONFIG")

    # Imports the main page, and error pages
    from .main import main as main_blueprint
    from .bookmark import bookmark as bookmark_blueprint
    app.register_blueprint(main_blueprint, url_prefix="/")
    app.register_blueprint(bookmark_blueprint, url_prefix="/bookmark")

    return app
