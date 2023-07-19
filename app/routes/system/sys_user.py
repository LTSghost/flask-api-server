
from app.services.sysUserService import sysUserService
from flask_restx import Resource
from . import ns_user


@ns_user.route('/getSysUser')
class getSysUser(Resource):
    def get(self):
        return sysUserService.getSysUser()