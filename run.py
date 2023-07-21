import config as _config
from flask import make_response, render_template
from app.blueprints.sys_user import blueprint as user
from flask_cors import CORS
from flask_restx import Resource
from app import app, api

from app.routes.system import system

@app.route('/swagger/')
def render_swagger_ui():
    return render_template('swagger-ui2.html', title='My API Documentation')

app.register_blueprint(user)
app.register_blueprint(system)

CORS(app)

@api.route('/hello')
class HelloResource(Resource):
    @api.doc(description='Description for Endpoint 2', tags=['Tag 2'])
    def get(self):
        return {'message': 'Hello, World!'}

@api.route('/root')
class HTMLResource(Resource):
    @api.doc(description='Description for Endpoint 1')
    def get(self):
        html_content = "<html><body><h1>Hello, HTML!</h1></body></html>"
        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html'
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=_config.server_port)
