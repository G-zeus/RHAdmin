from ..controllers.history import HistoryController
from flask import Blueprint, request
from ..utils.security import Security

controller = HistoryController()
history = Blueprint('history', __name__, url_prefix='/api/history')
security = Security()


@history.before_request
def before_request_func():
    if 'Authorization' not in request.headers.keys():
        return controller.custom_error(code=401, msg='Unauthorized')

    authorization = request.headers['Authorization']
    token = authorization.split(" ")[1]

    if not security.verify_jwt(token):
        return controller.custom_error(code=401, msg='Unauthorized')


@history.get('/employee/<int:employee>')
def register(employee: int):
    return controller.get_employee_history(employee_id=employee)
