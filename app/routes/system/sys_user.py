from flask import request
from app.services.sysUserService import sysUserService
from flask_restx import Resource
from . import ns_user
from app.models.system import res_validate, course_model


@ns_user.route('/getSysUser')
class getSysUser(Resource):
    def get(self):
        return sysUserService.getSysUser()
    
@ns_user.route('/validate')
class validateSysUser(Resource):
    @ns_user.expect(course_model)
    @ns_user.marshal_list_with(res_validate)
    def post(self):
        data = request.get_json()
        return sysUserService.validate(data)