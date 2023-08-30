from back.src.repositories.employee import EmployeeRepository
from .contracts.main_controller import MainController


class EmployeeController(MainController):

    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def get_employees(self):
        return self.success(data=self.employee_repository.all())
