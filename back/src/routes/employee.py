from ..controllers.employee import EmployeeController
from flask import Blueprint

controller = EmployeeController()
employee = Blueprint('employee', __name__, url_prefix='/api/employee')


@employee.get('/')
def get_employees():
    return controller.get_employees()

