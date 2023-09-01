from ..controllers.history import HistoryController
from flask import Blueprint, request

controller = HistoryController()
history = Blueprint('history', __name__, url_prefix='/api/history')


@history.get('/employee/<int:employee>')
def register(employee:int):

    return controller.get_employee_history(employee_id=employee)



