from flask import Blueprint
from flask_restx import Api, Resource
# from app.services import sysUserService

system = Blueprint('system', __name__)
sys_api = Api(
            system, version='1.0', 
            doc='/system/',
            title='System RESTful Service',
            description='System API',
            default_swagger_filename= 'system',
            prefix='/system'
        )

sys_ns = sys_api.namespace('sys_user', description='sys operations')

# @sys_ns.route('/getSysUser')
# class getSysUser(Resource):
#     def get(self):
#         return sysUserService.getSysUser()
