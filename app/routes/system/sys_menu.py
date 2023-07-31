from . import ns_menu
from flask import request
from flask_restx import Resource
from app.services.sysMenuService import sysMenuService
from app.models_api.system import menu_model, res_menu

@ns_menu.route('/test')
class getTest(Resource):
    def get(self):
        return {'message': 'test'}

@ns_menu.route('/menuInfo')
class validateSysUser(Resource):
    @ns_menu.expect(menu_model)
    # @ns_menu.marshal_list_with(res_menu)
    def post(self):
        print('doing menuINFO')
        data = request.get_json()
        return sysMenuService.menuInfo(data)