"""
Handles incoming request
"""

from flask import Flask, request, url_for, redirect
from routes import *

User.objects.create(email='user@email.com', password='password')

app = Flask(__name__)
app.register_blueprint(routes)
app.run(debug = True)
