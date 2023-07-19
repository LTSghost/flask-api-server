from flask_restx import Resource

# from .__init__ import MY_CONSTANT
# print(MY_CONSTANT)

# from .system import sys_role
# from .__init__ import sys_api
from . import nr


sys = 'sysRole'

@nr.route('/role')
class getRole(Resource):
    def get(self):
        return {'message': 'testRole'}

print('decorate role')