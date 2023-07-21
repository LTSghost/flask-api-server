import json
import datetime
import pandas as pd
import hashlib
# from flask import jsonify
from app.models.system import sys_user
from app import engine, app, db
from sqlalchemy import text

# class User:
def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class sysUserService:
    def getSysUser():
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_user"), connection)
        df_json = df.to_json(orient='records')
        connection.close()

        return json.loads(df_json)
    
    def getSysUserById(id):
        getUser = db.get_or_404(sys_user, id)
        print(getUser.USER_ID)
        print(getUser.PASSWORD)
        # jsonifyGet = jsonify(getUser)
        getUser = as_dict(getUser)
        print(getUser)

        return getUser
    
    def addSysUser(data):
        current = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        beforeMd5 = data['USER_ID']+data['PASSWORD']

        m = hashlib.md5()
        m.update(beforeMd5.encode("utf-8"))
        getHashData = m.hexdigest()

        user = sys_user(
            USER_ID=data['USER_ID'],
            USER_NAME=data['USER_NAME'],
            PASSWORD=getHashData,
            IS_VALID=data['IS_VALID'],
            CREATOR=data['CREATOR'],
            CREATE_TIME=current
        )
        db.session.add(user)
        db.session.commit()
        return {"good":'good'}

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

        try:
            getPWD = json.loads(df_json)[0]["PASSWORD"]
            print(getPWD)
        except Exception as e:
            app.logger.error(f"sys_user is not found: {e}")
            getPWD = ""

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
            resDict = {}
            resDict['Status'] = 'N'
            resDict['Message'] = '登入失敗'
            resDict['MessageId'] = 'LoginFailure'
            resDict['User'] = None
            print(resDict)

            return resDict

        return json.loads(df_json)