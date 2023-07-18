from flask import Blueprint
from flask_restx import Api, Resource
from app.services.sysUserService import sysUserService
from app.services.sysMenuService import sysMenuService

system = Blueprint('system', __name__)
sys_api = Api(
            system, version='1.0', 
            doc='/system/',
            title='System RESTful Service',
            description='System API',
            default_swagger_filename= 'system',
            prefix='/system'
        )

sys_user = sys_api.namespace('sys_user', description='sys operations')
sys_menu = sys_api.namespace('sys_menu', description='sys operations')

@sys_user.route('/getSysUser')
class getSysUser(Resource):
    def get(self):
        return sysUserService.getSysUser()
    
@sys_menu.route('/getSysMenu')
class getSysMenu(Resource):
    def get(self):
        return sysMenuService.getSysMenu()
