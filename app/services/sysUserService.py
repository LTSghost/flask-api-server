import json
import pandas as pd
from app import engine
from sqlalchemy import text

class sysUserService:
    def getSysUser():
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_user"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)