import config as _config
import sqlalchemy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# from app.models.system import sys_user

print('app')

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# --------------------------------------
from flask_restx import Api, Resource
api = Api(app, doc='/swagger-ui/', title='My swagger UI', prefix='/swagger-ui')

@api.route('/top-bar')
class TopBar(Resource):
    def get(self):
        # Handle GET request for the top bar
        return {'message': 'This is the top bar'}
#---------------------------------------


app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{_config.username}:{_config.password}@{_config.host}:{_config.port}/{_config.database}'

# build engine from sqlalchemy
engine = sqlalchemy.create_engine(
    f'mysql+pymysql://{_config.username}:{_config.password}@{_config.host}:{_config.port}/{_config.database}')

db = SQLAlchemy(app)

# Define a model for demonstration
# class sys_user(db.Model):
#     __tablename__   = 'sys_user'
#     USER_ID = db.Column(db.String(50), primary_key=True)
#     USER_NAME = db.Column(db.String(50), unique=True)
#     PASSWORD = db.Column(db.String(100))

from app.models.system import sys_user

# Execute raw SQL query
def get_users():
    query = text("SELECT * FROM sys_user")
    result = db.session.execute(query)
    users = []
    for row in result:
        user = sys_user(USER_ID=row.USER_ID, USER_NAME=row.USER_NAME, PASSWORD=row.PASSWORD)
        users.append(user.USER_ID)
        users.append(user.USER_NAME)
        users.append(user.PASSWORD)
    return users

with app.app_context():
    print(get_users())