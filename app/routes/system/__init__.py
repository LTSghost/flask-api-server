# import system as _system
from flask import Blueprint
from flask_restx import Api, Resource

# print('sys_role before')
# from . import sys_role as _sys_role
# print('sys_role after')

# from . import system as _system

# from .sys_role import sys

# _sys = sys

# _straa = system.aa
# _system = system.system
# _sys_api = system.sys_api

MY_CONSTANT = 42

system = Blueprint('system', __name__)
sys_api = Api(
            system, version='1.0', 
            doc='/system/',
            title='System RESTful Service',
            description='System API',
            default_swagger_filename= 'system',
            prefix='/system'
        )

nr = sys_api.namespace('sys_role', description='sys operations')
ns_user = sys_api.namespace('sys_user', description = 'sys_user operations')
print('My_system done')

# @sys_role.route('/role')
# class getRole(Resource):
#     def get(self):
#         return {'message': 'testRole'}

from . import sys_role as _sys_role
from . import sys_user as _sys_user