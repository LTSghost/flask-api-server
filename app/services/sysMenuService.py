import json
import pandas as pd
from app import engine
from sqlalchemy import text

class sysMenuService:
    def getSysMenu():
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_menu"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)
    
    def menuInfo(data):
        connection = engine.connect()

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



        connection.close()

        return json.loads(df_json)