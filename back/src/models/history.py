import datetime
from .base import db


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    values = db.Column(db.JSON)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=None, onupdate=datetime.datetime.utcnow)

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "values": self.values,
            "updated_at": str(self.updated_at),
            "created_at": str(self.created_at)
        }

    def get_session(self):
        return db.session
