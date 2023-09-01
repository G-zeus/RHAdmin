from flask_sqlalchemy.model import Model
from sqlalchemy.exc import NoResultFound
from typing import Any


class BaseRepository:

    def __init__(self, model: Model):
        self.model = model

    def all_by(self, **values: Any) -> list:
        data = self.model.query.filter_by(**values)
        return self.obj_to_dic(data)

    def all(self) -> list:
        data = self.model.query.all()
        return self.obj_to_dic(data)

    def get_one_by_id(self, id):
        try:
            return self.model.query.filter_by(id=id).one().obj_to_dict()
        except NoResultFound:
            return None

    def get_one(self, **values: Any):
        try:
            return self.model.query.filter_by(**values).one().obj_to_dict()
        except NoResultFound:
            return None

    def create(self, data):
        raise NotImplementedError

    def update(self, id, data):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError

    def obj_to_dic(self, obj: list) -> list:
        res = []
        for item in obj:
            res.append(item.obj_to_dict())
        return res
