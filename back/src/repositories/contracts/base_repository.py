from flask_sqlalchemy.model import Model
from sqlalchemy import insert


class BaseRepository:

    def __init__(self, model: Model):
        self.model = model

    def all(self) -> list:
        data = self.model.query.all()
        res = []
        for item in data:
            res.append(item.obj_to_dict())
        return res

    def get_one_by_id(self, id):
        data = self.model.query.get(id)
        if data is None:
            return None
        return data.obj_to_dict()

    def get_one(self, param):
        raise NotImplementedError

    def create(self, data):
        raise NotImplementedError

    def update(self, data):
        raise NotImplementedError

    def delete(self, data):
        raise NotImplementedError
