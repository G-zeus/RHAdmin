import json

from flask import Flask, Response
from .config.config import Config

app = Flask(__name__, instance_relative_config=True)


def create_app(test_config=None):
    get_config()

    # a simple page that says hello
    @app.route('/')
    def hello():
        return Response(response=json.dumps({'msg': 'RH Api running', 'code': 200}),
                        status=200,
                        mimetype='application/json')

    return app


def get_config():
    app.config.from_object(Config)

