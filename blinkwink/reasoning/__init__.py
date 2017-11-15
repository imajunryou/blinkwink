from flask import Blueprint

reasoning = Blueprint("reasoning", __name__)

from . import views
