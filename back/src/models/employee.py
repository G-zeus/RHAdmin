import datetime
from .base import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(200))
    second_name = db.Column(db.String(200))
    emergency_contact = db.Column(db.String(250))
    emergency_phone = db.Column(db.String(20))
    blood_type = db.Column(db.String(5))
    position = db.Column(db.String(20))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=None, onupdate=datetime.datetime.utcnow)

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.second_name,
            "second_name": self.second_name,
            "emergency_contact": self.emergency_contact,
            "emergency_phone": self.emergency_phone,
            "blood_type": self.blood_type,
            "position": self.position,
            "updated_at": str(self.updated_at),
            "created_at": str(self.created_at)
        }

    def get_session(self):
        return db.session
