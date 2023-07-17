import json
import pandas as pd
from sqlalchemy import text
from flask import Flask, make_response
from app.blueprints.basic_endpoints import blueprint as basic_endpoints
from app.blueprints.sys_user import blueprint as sys_user
from app import engine
from flask_cors import CORS
from flask_restx import Api, Resource, fields


app = Flask(__name__)
app.register_blueprint(basic_endpoints)
app.register_blueprint(sys_user)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API')

ns = api.namespace('todos', description='TODO operations')

CORS(app)

@ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

# @ns.route('/')
# class home(Resource):
#    def get(self):
#        reutnr '<h1>Hello Flask</h1>'

@ns.route('/')
class HTMLResource(Resource):
    def get(self):
        html_content = "<html><body><h1>Hello, HTML!</h1></body></html>"
        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html'
        return response

@app.route('/getUsers')
def getUsers():
    print('getUsers from sqlalchemy engine')
    connection = engine.connect()

    cursor = connection.execute(text("select * from sys_user"))
    getCursor = cursor.fetchall()

    df = pd.read_sql(text("select * from sys_menu"), connection)
    df_json = df.to_json(orient='records')
    connection.close()

    return json.loads(df_json)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port='7777')
