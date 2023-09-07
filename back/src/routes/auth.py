from ..controllers.auth import AuthController
from flask import Blueprint, request
from cerberus import Validator
from ..schemas.login import logging_schema
from ..schemas.register import register_schema
from ..utils.sanitizer import sanitize

controller = AuthController()
v = Validator()
auth = Blueprint('auth', __name__, url_prefix='/api')


@auth.post('/register')
def register():
    request_data = sanitize(request.get_json())
    v.schema = register_schema
    if not v.validate(request_data):
        return controller.custom_error(msg='validation error', errors=v.errors, code=400)

    return controller.register(request_data)


@auth.post('/login')
def login():
    request_data = sanitize(request.get_json())
    v.schema = logging_schema
    if not v.validate(request_data):
        return controller.custom_error(msg='validation error', errors=v.errors, code=400)

    return controller.login(request_data)


@auth.post('/logout')
def logout():
    return controller.custom_error(msg='validation error', errors=v.errors, code=400)
