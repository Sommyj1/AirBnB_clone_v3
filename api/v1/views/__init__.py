#!/usr/bin/python3
"""The RESTful API module.

This houses the blueprint for our Flask app.

"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
