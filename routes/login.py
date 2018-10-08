"""
Handles incoming request
"""

from datetime import datetime, timedelta
from flask import request, jsonify, make_response
from . import routes
from models.user import User
from middlewares.auth import generate_jwt

@routes.route('/login', methods=['POST', 'GET'])
@generate_jwt
def login():
    """
    Login API
    """
    if request.method == 'POST':
        user_name = request.headers.get("username")
        password = request.headers.get("password")
        if user_name is None:
            return "username not present", 400
        elif password is None:
            return "password not present", 400
        
        try:
            user = User.objects.get(email=user_name)
            user.match_password(password)
        except (User.DoesNotExist, User.PasswordDoesNotMatch):
            return "Wrong credentials", 400

        pay_load = {
            'user_id': user.id
        }
        return make_response("login successful"),pay_load

    elif request.method == "GET":
        return "Login Page"