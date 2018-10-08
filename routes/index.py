from flask import render_template
from . import routes
from decorators.auth import authorize

@routes.route('/')
def index():
    return "index"

@routes.route('/test')
@authorize
def home_page():
    """
    Testing
    """
    return "hello"

@routes.route('/data')
@authorize
def home_page1():
    """
    Testing
    """
    return "bye"