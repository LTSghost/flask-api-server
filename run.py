# import json
# import pandas as pd
# from sqlalchemy import text
from flask import make_response, render_template
from app.blueprints.basic_endpoints import blueprint as basic_endpoints
from app.blueprints.sys_user import blueprint as sys_user
from app.routes.sys_user import system
# from app import engine
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from app import app, api

print("run.py")

@app.route('/swagger')
def render_swagger_ui():
    return render_template('swagger-ui2.html', title='My API Documentation')

# app.register_blueprint(basic_endpoints)
app.register_blueprint(sys_user)
app.register_blueprint(system)

CORS(app)

# @ns.route('/hello')
@api.route('/hello')
class HelloResource(Resource):
    @api.doc(description='Description for Endpoint 2', tags=['Tag 2'])
    def get(self):
        return {'message': 'Hello, World!'}

# @ns.route('/')
# class home(Resource):
#    def get(self):
#        reutnr '<h1>Hello Flask</h1>'

# @ns.route('/')
@api.route('/root')
class HTMLResource(Resource):
    @api.doc(description='Description for Endpoint 1')
    def get(self):
        html_content = "<html><body><h1>Hello, HTML!</h1></body></html>"
        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html'
        return response

# @app.route('/getUsers')
# def getUsers():
#     print('getUsers from sqlalchemy engine')
#     connection = engine.connect()

#     cursor = connection.execute(text("select * from sys_user"))
#     getCursor = cursor.fetchall()

#     df = pd.read_sql(text("select * from sys_menu"), connection)
#     df_json = df.to_json(orient='records')
#     connection.close()

#     return json.loads(df_json)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port='7777')
