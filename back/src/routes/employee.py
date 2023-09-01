from ..controllers.employee import EmployeeController
from flask import Blueprint, request
from cerberus import Validator
from ..schemas.amployee_create import employee_create_schema
from ..schemas.amployee_update import employee_update_schema

controller = EmployeeController()
v = Validator()
employee = Blueprint('employee', __name__, url_prefix='/api/employee')


@employee.get('/')
def get_employees():
    return controller.get_employees()


@employee.get('/<int:id>')
def get_error(id: int):
    return controller.get_employee(id)


@employee.post('/')
def create():
    request_data = request.get_json()
    v.schema = employee_create_schema
    if v.validate(request_data):
        return controller.create(request_data)

    return controller.custom_error(msg='validation error', errors=v.errors, code=400)


@employee.patch('//<int:id>')
def update(id: int):
    request_data = request.get_json()
    v.schema = employee_update_schema
    if v.validate(request_data):
        return controller.update(id, request_data)

    return controller.custom_error(msg='validation error', errors=v.errors, code=400)


@employee.delete('/<int:id>')
def delete(id: int):
    return controller.delete(id)
