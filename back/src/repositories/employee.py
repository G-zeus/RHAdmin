from .contracts.base_repository import BaseRepository
from ..models.employee import Employee


class EmployeeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Employee())
        self.session = Employee().get_session()

    def create(self, data):
        # print(data['name'])
        e = Employee(name=data['name'],
                     last_name=data['last_name'],
                     second_name=data['second_name'],
                     emergency_contact=data['emergency_contact'],
                     emergency_phone=data['emergency_phone'],
                     blood_type=data['blood_type'] if data['blood_type'] is not None else None,
                     position=data['position'])

        self.session.add(e)
        self.session.commit()

        return e.obj_to_dict()
