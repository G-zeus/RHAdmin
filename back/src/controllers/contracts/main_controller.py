from flask import jsonify, Response
from ...repositories.user import UserRepository
import json


class MainController:

    def getAuth(self, id: int):
        user_repo = UserRepository()
        return user_repo.get_one_by_id(id)

    def success(self, msg: str = 'success', data: json = None):
        if data is None:
            data = []

        return Response(response=json.dumps({'msg': msg, 'code': 200, 'data': data}),
                        status=200,
                        headers={'Access-Control-Allow-Origin': '*'},
                        mimetype='application/json')

    def error(self, msg: str = 'error'):
        return Response(response=json.dumps({'msg': msg, 'code': 500}),
                        status=500,
                        headers={'Access-Control-Allow-Origin': '*'},
                        mimetype='application/json')

    def not_found(self, msg: str = 'not found'):
        return Response(response=json.dumps({'msg': msg, 'code': 400}),
                        status=400,
                        headers={'Access-Control-Allow-Origin': '*'},
                        mimetype='application/json')

    def custom_error(self, code=505, msg: str = 'error custom', errors: json = None):
        if errors is None:
            errors = []
        return Response(response=json.dumps({'msg': msg, 'code': code, 'error_bag': errors}),
                        status=code,
                        headers={'Access-Control-Allow-Origin': '*'},
                        mimetype='application/json')
