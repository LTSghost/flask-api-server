import json
from app.routes.system import sys_api, fields


# user
addUser_model = sys_api.model("addUser_model", {
    "USER_ID": fields.String,
    "USER_NAME": fields.String,
    "PASSWORD": fields.String,
    "IS_VALID":fields.String,
    "CREATOR":fields.String
})
login_model = sys_api.model("login_model", {
    "USER_ID": fields.String,
    "PASSWORD": fields.String
})
json_object = json.dumps({
    "id": "04",
    "name": "sunil",
    "department": "HR"
})
res_validate = sys_api.model("res_validate", {
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

# menu
menu_model = sys_api.model("menu_model", {
    "USER_ID": fields.String,
    "USER_NAME": fields.String
})