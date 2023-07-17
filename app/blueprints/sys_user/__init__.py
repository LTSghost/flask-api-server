from flask import Blueprint, request
from flask_restx import Api, Resource
from sqlalchemy import text
from app.models.database import engine
import json
import pandas as pd

blueprint = Blueprint('user', __name__)
api = Api(blueprint, version='1.0', title='Flask-API RESTful Service', description='sys_user API',
          default_swagger_filename= 'system')
# api2 = Api(blueprint, version='1.0', title='Flask-API RESTful Service', description='sys_user API',
#           default_swagger_filename= 'system2')
ns = api.namespace('sys_user', description='sys operations')
ns2 = api.namespace('sys_user2', description='sys operations')

# @blueprint.route('/sys_user', methods=['GET'])
# def getSysUser():
#     if request.method == 'GET':
#         connection = engine.connect()

#         df = pd.read_sql(text("select * from sys_user"), connection)
#         df_json = df.to_json(orient='records')
#         connection.close()

#         return json.loads(df_json)

@ns.route('/getSysUser')
class getSysUser(Resource):
    def get(self):
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_user"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)

@ns2.route('/getSysUser2')
class getSysUser(Resource):
    def get(self):
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_user"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)
