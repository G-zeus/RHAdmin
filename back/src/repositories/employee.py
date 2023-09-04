import json

from .contracts.base_repository import BaseRepository
from ..models.employee import Employee
from ..models.employee import History
from sqlalchemy.exc import NoResultFound


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

    def update(self, id, data):
        try:
            old = self.model.query.filter_by(id=id).one()

            old_dict = old.obj_to_dict()

            changes = {k: {'old_value': old_dict[k], 'new_value': data[k]} for k, v in data.items() if
                       old_dict[k] != data[k]}
            for k, v in changes.items():
                setattr(old, k, v['new_value'])

            self.session.add(old)
            self.session.commit()

            if len(changes) > 0:
                h = History(values=json.dumps(changes), employee_id=old.id)
                self.session.add(h)
                self.session.commit()

            return old.obj_to_dict()
        except Exception as e:
            return e.__repr__()

    def delete(self, id):
        try:
            row = self.model.query.filter_by(id=id).one()
            row.is_active = False
            changes = {'is_active': {'old_value': row.is_active, 'new_value': row.is_active}}
            self.session.add(row)
            self.session.commit()

            h = History(values=json.dumps(changes), employee_id=row.id)
            self.session.add(h)
            self.session.commit()

            return {"id": row.id, 'deleted': True}

        except NoResultFound:
            return None

    def get_emergency_info(self, id: int):
        try:
            row = self.model.query.filter_by(id=id).one()

            return {
                "id": row.id,
                "emergency_contact": row.emergency_contact,
                "emergency_phone": row.emergency_phone,
                "blood_type": row.blood_type,
            }

        except NoResultFound:
            return None
