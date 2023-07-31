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
    "MENU_ID": fields.String
})
res_menu = sys_api.model("res_menu",{
    "MENU_ID": fields.String,
    "MENU_NAME": fields.String,
    "P_MENU_ID": fields.String,
    "SEQ_NO": fields.String,
    "PAGE": fields.String,
    "ICON": fields.String,
    "PATH": fields.String,
    "children": fields.Raw(json.dumps({
        "MENU_ID_B": "string",
        "MENU_NAME_B": "string",
        "P_MENU_ID_B": "string",
        "SEQ_NO_B": "string",
        "ICON_B": "string",
        "PATH_B": "string",
        "CREATOR_B": "string",
        "CREATE_TIME_B": "string",
        "UPDATER_B": "string",
        "UPDATE_TIME_B": "string",
        "BREADCRUMB_B": "string"
    })),
    "BREADCRUMB": fields.String,
    "CREATOR": fields.String,
    "CREATE_TIME": fields.String,
    "UPDATER": fields.String,
    "UPDATE_TIME": fields.String
})