from flask import Flask
from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config.from_envvar("BLINKWINK_CONFIG")

    # Imports the main page, and error pages
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix="/")

    from .reasoning import reasoning as reasoning_blueprint
    app.register_blueprint(reasoning_blueprint, url_prefix="/reasoning")

    return app
