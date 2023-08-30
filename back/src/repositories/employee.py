from .contracts.base_repository import BaseRepository
from back.src.models.employee import Employee


class EmployeeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Employee())

