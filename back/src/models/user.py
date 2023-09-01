import datetime
from .base import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=None, onupdate=datetime.datetime.utcnow)

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "email": self.email,
            "updated_at": str(self.updated_at),
            "created_at": str(self.created_at)
        }

    def get_session(self):
        return db.session
