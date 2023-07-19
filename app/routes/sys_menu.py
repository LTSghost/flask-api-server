from .sys_user import sys_api
from flask_restx import Resource

sys_menu = sys_api.namespace('sys_menu', description='sys operations')

@sys_menu.route('/test')
class getTest(Resource):
    def get(self):
        return {'message': 'test'}
