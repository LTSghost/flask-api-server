from flask import Blueprint
from flask_restx import Api, Resource

sys_user_route= Blueprint('sys_user', __name__)

api = Api(sys_user_route, version='1.0', title='Flask-API RESTful Service', description='sys_user API',
          default_swagger_filename= 'system/sys_user')

ns = api.namespace('sys_user', description='sys operations')

