import json

from .contracts.base_repository import BaseRepository
from ..models.history import History
from sqlalchemy.exc import NoResultFound


class HistoryRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, History())
        self.session = History().get_session()

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




