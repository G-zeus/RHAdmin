from ..repositories.employee import EmployeeRepository
from .contracts.main_controller import MainController
from ..utils.qr import QR
from flask import send_file


class EmployeeEmergencyInfoController(MainController):

    def __init__(self):
        self.employee_repository = EmployeeRepository()
        self.qr = QR()

    def get_emergency_info(self, id: int) -> object:
        data = self.employee_repository.get_emergency_info(id=id)

        if data is None:
            return self.error("Employee not found")

        return self.success(data=data)

    def get_qr_image(self, id: int):
        uri = "#/infoEmergencia/" + str(id)
        print("id: "+str(id)+ "  uri:" +uri)

        self.qr.make_qr(uri)
        name = uri.replace('/', '_')+'.png'
        return send_file(path_or_file='../var/storage/' + name,
                         mimetype="image/png",
                         as_attachment=True,
                         download_name=name)
