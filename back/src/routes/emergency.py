from ..controllers.employee_emergency_info import EmployeeEmergencyInfoController
from flask import Blueprint, request

controller = EmployeeEmergencyInfoController()
emergency = Blueprint('emergency', __name__, url_prefix='/api/emergency')


@emergency.get('/<int:id>')
def get_emergency_info(id: int):
    return controller.get_emergency_info(id=id)


@emergency.get('/qr/<int:id>')
def get_qr_image(id: int):
    return controller.get_qr_image(id=id)
