import json

from flask import Flask, Response

from .config.config import Config
from .routes.employee import employee

app = Flask(__name__, instance_relative_config=True)


def create_app(test_config=None):
    get_config()
    set_db()
    get_routes()

    # a simple page that says hello
    @app.route('/')
    def hello():
        return Response(response=json.dumps({'msg': 'RH Api running', 'code': 200}),
                        status=200,
                        mimetype='application/json')

    return app


def get_config():
    app.config.from_object(Config)


def get_routes():

    app.register_blueprint(employee)

def set_db():
    from . import models as database
    database.init_app(app)
    database.create_all(app)
