from flask import request
from app.services.sysUserService import sysUserService
from flask_restx import Resource
from . import ns_user
from app.models_api.system import res_validate, login_model, addUser_model

@ns_user.route('/validate')
class validateSysUser(Resource):
    @ns_user.expect(login_model)
    @ns_user.marshal_list_with(res_validate)
    def post(self):
        data = request.get_json()
        return sysUserService.validate(data)

@ns_user.route('')
class getSysUser(Resource):
    def get(self):
        return sysUserService.getSysUser()
    
    # def create(self):
    #     data = request.get_json()
    #     return sysUserService.addSysUser(data)

    @ns_user.expect(addUser_model)
    def post(self):
        data = request.get_json()
        return sysUserService.addSysUser(data)
    
    @ns_user.expect(addUser_model)
    def put(self):
        data = request.get_json()
        return sysUserService.modifySysUser(data)
    
    @ns_user.expect(login_model)
    def delete(self):
        data = request.get_json()
        return sysUserService.delSysUser(data)
    
@ns_user.route('/<id>')
@ns_user.doc(params={'id': 'USER_ID'})
class getSysUserById(Resource):
    def get(self, id):
        print('by Id')  
        return sysUserService.getSysUserById(id)

