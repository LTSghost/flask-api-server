from flask import Blueprint
from flask_restx import Api, Resource

print('system')

aa = 'bb'
bb = 'cc'
system = Blueprint('system', __name__)
sys_api = Api(
            system, version='1.0', 
            doc='/system/',
            title='System RESTful Service',
            description='System API',
            default_swagger_filename= 'system',
            prefix='/system'
        )

sys_role = sys_api.namespace('sys_role', description='sys operations')

@sys_api.route('/root')
class getRoot(Resource):
    def get(self):
        return {'message': 'is root'}