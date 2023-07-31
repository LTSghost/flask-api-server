import json
import pandas as pd
from app import engine
from sqlalchemy import text
from app.models.system import build_sys_menu_final_tree

class sysMenuService:
    def getSysMenu():
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_menu"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)
    
    def menuInfo(data):
        connection = engine.connect()

        print(data['MENU_ID'])

        df = pd.read_sql(text(f"""
        select
            A.*,
            B.MENU_ID as MENU_ID_B, B.MENU_NAME as MENU_NAME_B, B.P_MENU_ID as P_MENU_ID_B,
            B.SEQ_NO as SEQ_NO_B,B.ICON as ICON_B, B.PATH as PATH_B,
            B.CREATOR as CREATOR_B, B.CREATE_TIME as CREATE_TIME_B,
            B.UPDATER as UPDATER_B, B.UPDATE_TIME as UPDATE_TIME_B,
            CONCAT(B.P_MENU_ID,'@',A.ICON,'@@',B.MENU_ID,'@',B.ICON,'@',B.PATH) AS BREADCRUMB_B
        from (select * from sys_menu where isnull(P_MENU_ID)) A
        join (select * from sys_menu where !isnull(P_MENU_ID)) B on A.MENU_ID=B.P_MENU_ID
        where LOWER(A.MENU_ID) like LOWER(CONCAT('%',\"{data['MENU_ID']}\",'%'));"""), connection)

        # Convert a specific column to string
        df['CREATE_TIME'] = df['CREATE_TIME'].astype(str)
        df['CREATE_TIME_B'] = df['CREATE_TIME'].astype(str)
        df['UPDATE_TIME'] = df['UPDATE_TIME'].astype(str)
        df['UPDATE_TIME_B'] = df['UPDATE_TIME'].astype(str)

        df_json = df.to_json(orient='records')

        print('aab')
        print(json.loads(df_json))
        print(df)

        menu = set()
        for el in json.loads(df_json):
            
            menu.add(el['MENU_ID'])
            
            if el['P_MENU_ID_B'] in menu:
                el['children'] = {el['MENU_ID_B']}

        def transfer_keys(data):
            new_data = {}
            for key, value in data.items():
                if key.endswith("_B"):
                    new_key = key.replace("_B", "")
                    new_data.setdefault("children", {})[new_key] = value
                else:
                    new_data[key] = value
            return new_data

        # result = transfer_keys(json.loads(df_json)) 
        # print(result)
        
        recordList = []
        newList = []
        for el in json.loads(df_json):

            if el["MENU_ID"] not in recordList:
                recordList.append(el["MENU_ID"])

                newList.append(transfer_keys(el))
            else:
                getIndex = recordList.index(el["MENU_ID"])
                newList[getIndex]['children']

            
        
        return newList
            
        
            

        connection.close()

        resDict = {}
        resDict['MENU_ID']=''

        # result = build_sys_menu_final_tree(json.loads(df_json))
        # return result

        # for k,v in json.loads(df_json)[0].items():
        #     print(k)

        return json.loads(df_json)