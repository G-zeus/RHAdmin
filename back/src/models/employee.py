import datetime
from .base import db


class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    second_name = db.Column(db.String(200))
    emergency_contact = db.Column(db.String(250))
    emergency_phone = db.Column(db.String(20))
    blood_type = db.Column(db.String(5))
    position = db.Column(db.String(20))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=None, onupdate=datetime.datetime.utcnow)

