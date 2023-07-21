import json
from app.routes.system import sys_api, fields

add_model = sys_api.model("add_model", {
    "USER_ID": fields.String,
    "USER_NAME": fields.String,
    "PASSWORD": fields.String,
    "IS_VALID":fields.String,
    "CREATOR":fields.String
})

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