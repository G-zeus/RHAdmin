from ..controllers.employee import EmployeeController
from flask import Blueprint, request

controller = EmployeeController()
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
    return controller.create(request_data)
