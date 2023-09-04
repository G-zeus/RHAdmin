import json

from flask import Flask, Response

from .config.config import Config
from .routes.employee import employee
from .routes.auth import auth
from .routes.history import history
from .routes.emergency import emergency

app = Flask(__name__, instance_relative_config=True)


def create_app(test_config=None):
    get_config()
    set_db()
    set_cors()
    get_routes()

    # a simple page that says hello
    @app.route('/')
    def hello():
        return Response(response=json.dumps({'msg': 'RH Api running', 'code': 200}),
                        status=200,
                        headers={'Access-Control-Allow-Origin': '*'},
                        mimetype='application/json')

    return app


def get_config():
    # app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(Config)



def get_routes():
    app.register_blueprint(employee)
    app.register_blueprint(auth)
    app.register_blueprint(history)
    app.register_blueprint(emergency)


def set_db():
    from . import models as database
    database.init_app(app)
    database.create_all(app)


def set_cors():
    from . import routes as routes

    routes.init_app(app)
