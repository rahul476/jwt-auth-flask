import jwt
import yaml
from flask import request, redirect, make_response
from datetime import datetime, timedelta

with open("data/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

JWT_SECRET = cfg['JWT_SECRET']
JWT_ALGORITHM = cfg['JWT_ALGORITHM']
JWT_EXP_DELTA_SECONDS = cfg['JWT_EXP_DELTA_SECONDS']

def authorize(func):
    """
    Middleware
    """
    def decorated_function(*args, **kwargs):
        jwt_token = request.cookies.get("jwt_token")
        if jwt_token is None:   
            return redirect("/")   

        try:
            payload = jwt.decode(jwt_token, JWT_SECRET,algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return "Token is invalid", 400

        return func(*args, **kwargs)

    decorated_function.__name__  = func.__name__ 
    return decorated_function

def generate_jwt(func):
    """
    Middleware
    """
    def decorated_function(*args, **kwargs):
        response, pay_load = func(*args, **kwargs)
        pay_load["exp"]=datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        jwt_token = jwt.encode(pay_load, JWT_SECRET, JWT_ALGORITHM)
        response.set_cookie("jwt_token",jwt_token)
        return response

    decorated_function.__name__  = func.__name__ 
    return decorated_function
