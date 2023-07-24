from flask import Blueprint

aitools_app = Blueprint('aitools_app', __name__)

from . import views