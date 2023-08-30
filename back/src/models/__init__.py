from .base import db


def init_app(app):
    db.init_app(app)


def create_all(app):
    with app.app_context():
        db.create_all()
