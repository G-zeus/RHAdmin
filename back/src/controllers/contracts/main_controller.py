from flask import jsonify, Response
import json


class MainController:

    def success(self, msg: str = 'success', data: json = None):
        if data is None:
            data = []

        return Response(response=json.dumps({'msg': msg, 'code': 200, 'data': data}),
                        status=200,
                        mimetype='application/json')

    def error(self, msg: str = 'error'):
        return Response(response=json.dumps({'msg': msg, 'code': 500}),
                        status=500,
                        mimetype='application/json')

    def not_found(self, msg: str = 'not found'):
        return Response(response=json.dumps({'msg': msg, 'code': 400}),
                        status=400,
                        mimetype='application/json')

    def custom_error(self, code=505, msg: str = 'error custom', errors: json = None):
        if errors is None:
            errors = []
        return Response(response=json.dumps({'msg': msg, 'code': code, 'error_bag': errors}),
                        status=code,
                        mimetype='application/json')