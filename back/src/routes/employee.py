from ..controllers.employee import EmployeeController
from flask import Blueprint, request
from cerberus import Validator
from ..utils.security import Security
from ..utils.sanitizer import sanitize
from ..schemas.amployee_create import employee_create_schema
from ..schemas.amployee_update import employee_update_schema

controller = EmployeeController()
v = Validator()
employee = Blueprint('employee', __name__, url_prefix='/api/employee')
security = Security()
# request_data = sanitize(request.get_json())


@employee.before_request
def before_request_func():
    if request.method != 'OPTIONS':

        if 'Authorization' not in request.headers.keys():
            return controller.custom_error(code=401, msg='Unauthorized')

        authorization = request.headers['Authorization']
        token = authorization.split(" ")[1]

        valid_token = security.verify_jwt(token)

        if not valid_token:
            return controller.custom_error(code=401, msg='Unauthorized')

        if not controller.getAuth(valid_token['user']):
            return controller.custom_error(code=401, msg='Unauthorized')



@employee.get('/')
def get_employees():
    return controller.get_employees()


@employee.get('/<int:id>')
def get_error(id: int):
    return controller.get_employee(id)


@employee.post('/')
def create():
    request_data = sanitize(request.get_json())
    v.schema = employee_create_schema
    if v.validate(request_data):
        return controller.create(request_data)

    return controller.custom_error(msg='validation error', errors=v.errors, code=400)


@employee.patch('//<int:id>')
def update(id: int):
    request_data = sanitize(request.get_json())
    v.schema = employee_update_schema
    if v.validate(request_data):
        return controller.update(id, request_data)

    return controller.custom_error(msg='validation error', errors=v.errors, code=400)


@employee.delete('/<int:id>')
def delete(id: int):
    return controller.delete(id)
