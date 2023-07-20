import json
from app import db
from app.routes.system import sys_api, fields

class s_user(db.Model):
    __tablename__   = 's_user'
    USER_ID = db.Column(db.String(50), primary_key=True)
    USER_NAME = db.Column(db.String(50), unique=True)
    PASSWORD = db.Column(db.String(100))

class validate(db.Model):
    a = db.Column(db.String(50), primary_key=True)

course_model = sys_api.model("course", {
    "USER_ID": fields.String,
    "PASSWORD": fields.String
})
json_object = json.dumps({
    "id": "04",
    "name": "sunil",
    "department": "HR"
})
res_validate = sys_api.model("validate", {
    "MessageId": fields.String,
    "Message": fields.String,
    "Status": fields.String,
    "User": fields.Raw(json.dumps({
        "USER_ID": "string",
        "USER_NAME": "string",
        "PASSWORD": "string",
        "IS_VALID": "string",
        "CREATOR": "string",
        "CREATE_TIME": "string",
        "UPDATER": "string",
        "UPDATE_TIME": "string"
    }))
})