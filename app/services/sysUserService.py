import json
import pandas as pd
import hashlib
from app import engine
from sqlalchemy import text

class sysUserService:
    def getSysUser():
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_user"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)
    
    def validate(data):
        print(data)
        print(type(data))
        print(data['USER_ID'])
        print(type(data['USER_ID']))

        beforeMd5 = data['USER_ID']+data['PASSWORD']

        connection = engine.connect()

        df = pd.read_sql(text(f"select * from sys_user where USER_ID='{data['USER_ID']}'"), connection)
        # df = pd.read_sql(text(f"select * from sys_user"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        getPWD = json.loads(df_json)[0]["PASSWORD"]
        print(getPWD)

        m = hashlib.md5()
        m.update(beforeMd5.encode("utf-8"))
        getHashData = m.hexdigest()
        # getHashData = "0"
        # getHashData= hashlib.md5().update(data['USER_ID']+data['PASSWORD']).hexdigest()

        if getPWD == getHashData:
            resDict = {}
            resDict['Status'] = 'Y'
            resDict['Message'] = '登入成功'
            resDict['MessageId'] = 'LoginSuccess'
            resDict['User'] = json.loads(df_json)[0]
            print(resDict)
            # return json.loads(df_json)[0]
            return resDict
        else:
            return {"Status": "N"}

        return json.loads(df_json)