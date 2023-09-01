from ..repositories.history import HistoryRepository
from .contracts.main_controller import MainController


class HistoryController(MainController):

    def __init__(self):
        self.history_repository = HistoryRepository()

    def get_employee_history(self, employee_id: int):
        return self.success(data=self.history_repository.all_by(employee_id=employee_id))
