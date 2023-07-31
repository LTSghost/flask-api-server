# import json
from app import db
# from app.routes.system import sys_api, fields

class sys_user(db.Model):
    __tablename__   = 'sys_user'
    USER_ID = db.Column(db.String(50), primary_key=True)
    USER_NAME = db.Column(db.String(100), unique=True)
    PASSWORD = db.Column(db.String(100))
    IS_VALID = db.Column(db.String(1))
    CREATOR = db.Column(db.String(50))
    CREATE_TIME = db.Column(db.DateTime)
    UPDATER = db.Column(db.String(50))
    UPDATE_TIME = db.Column(db.DateTime)

class validate(db.Model):
    a = db.Column(db.String(50), primary_key=True)

# course_model = sys_api.model("course", {
#     "USER_ID": fields.String,
#     "PASSWORD": fields.String
# })
# json_object = json.dumps({
#     "id": "04",
#     "name": "sunil",
#     "department": "HR"
# })
# res_validate = sys_api.model("validate", {
#     "MessageId": fields.String,
#     "Message": fields.String,
#     "Status": fields.String,
#     "User": fields.Raw(json.dumps({
#         "USER_ID": "string",
#         "USER_NAME": "string",
#         "PASSWORD": "string",
#         "IS_VALID": "string",
#         "CREATOR": "string",
#         "CREATE_TIME": "string",
#         "UPDATER": "string",
#         "UPDATE_TIME": "string"
#     }))
# })

class sys_menu(db.Model):
    MENU_ID = db.Column(db.String(50), primary_key=True)
    MENU_NAME = db.Column(db.String(100))
    P_MENU_ID = db.Column(db.String(50), db.ForeignKey('sys_menu.MENU_ID'))
    SEQ_NO = db.Column(db.Integer)
    ICON = db.Column(db.String(50))
    PATH = db.Column(db.String(100))
    PAGE = db.Column(db.String(100))
    BREADCRUMB = db.Column(db.String(200))
    CREATOR = db.Column(db.String(50))
    CREATE_TIME = db.Column(db.DateTime)
    UPDATER = db.Column(db.String(50))
    UPDATE_TIME = db.Column(db.DateTime)

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime

@dataclass
class SysMenuFinal:
    MENU_ID: str
    MENU_NAME: str
    P_MENU_ID: str
    SEQ_NO: str
    PAGE: str
    ICON: str
    PATH: str
    # children: List['SysMenuFinal']
    # BREADCRUMB: str
    CREATOR: str
    CREATE_TIME: datetime
    UPDATER: str
    UPDATE_TIME: datetime
    MENU_ID_B: str
    MENU_NAME_B: str
    P_MENU_ID_B: str
    SEQ_NO_B: str
    ICON_B: str
    PATH_B: str
    CREATOR_B: str
    CREATE_TIME_B: datetime
    UPDATER_B: str
    UPDATE_TIME_B: datetime
    BREADCRUMB_B: str

    def getPage(self) -> str:
        return f"pages/{self.PATH}.vue"
    
def build_sys_menu_final_tree(menu_list: List[Dict]) -> List[SysMenuFinal]:
    menu_dict = {menu['MENU_ID']: SysMenuFinal(**menu) for menu in menu_list}
    root_menus = []

    for menu in menu_list:
        if menu['MENU_ID'] is None:
            root_menus.append(menu_dict[menu['MENU_ID']])
        else:
            parent_menu = menu_dict[menu['P_MENU_ID']]
            if not hasattr(parent_menu, 'children'):
                parent_menu.children = []
            parent_menu.children.append(menu_dict[menu['MENU_ID']])

    return root_menus