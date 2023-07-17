import os
import sqlalchemy as db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# 連線 MYSQL
username = os.environ.get("MYSQL_USERNAME")  # 資料庫帳號
password = os.environ.get("MYSQL_PASSWORD")  # 資料庫密碼
host = os.environ.get("MYSQL_DB_ADDRESS")    # 資料庫位址
port = os.environ.get("MYSQL_PORT")          # 資料庫埠號
database = os.environ.get("MYSQL_DB")        # 資料庫名稱

app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# build engine from sqlalchemy
engine = db.create_engine(
    f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

db = SQLAlchemy(app)

# Define a model for demonstration
class sys_user(db.Model):
    __tablename__   = 'sys_user'
    USER_ID = db.Column(db.String(50), primary_key=True)
    USER_NAME = db.Column(db.String(50), unique=True)
    PASSWORD = db.Column(db.String(100))

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