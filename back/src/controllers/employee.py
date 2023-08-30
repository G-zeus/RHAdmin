from ..repositories.employee import EmployeeRepository
from .contracts.main_controller import MainController


class EmployeeController(MainController):

    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def get_employees(self):
        return self.success(data=self.employee_repository.all())

    def get_employee(self, id: int):
        return self.success(data=self.employee_repository.get_one_by_id(id))

    def create(self, data):
        row = self.employee_repository.create(data)

        return row
