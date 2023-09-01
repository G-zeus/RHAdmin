import json

from .contracts.base_repository import BaseRepository
from ..models.user import User
from sqlalchemy.exc import NoResultFound


class UserRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, User())
        self.session = User().get_session()

    def create(self, data):
        # print(data['name'])
        e = User(email=data['email'],
                 password=data['password'])

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

            return old.obj_to_dict()
        except Exception as e:
            return e.__repr__()

    def get_user_to_authenticate(self, **credentials):
        try:
            return self.model.query.filter_by(**credentials).one()
        except NoResultFound:
            return None



