from .contracts.base_repository import BaseRepository
from ..models.employee import Employee


class EmployeeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Employee())
        self.session = Employee().get_session()

    def create(self, data):
        # print(data['name'])
        e = Employee(name=data['name'], price=data['price'])

        self.session.add(e)
        self.session.commit()

        return e.obj_to_dict()


