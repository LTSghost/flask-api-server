import json
import datetime
import pandas as pd
import hashlib
# from flask import jsonify
from app.models.system import sys_user
from app import engine, app, db
from sqlalchemy import text
from pymysql.err import DataError
# from .interface import sysUserInterface


# class User:
def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class sysUserService():
    def getSysUser():
        connection = engine.connect()

        df = pd.read_sql(text("select * from sys_user"), connection)

        # Convert a specific column to string
        df['CREATE_TIME'] = df['CREATE_TIME'].astype(str)
        df['UPDATE_TIME'] = df['UPDATE_TIME'].astype(str)

        df_json = df.to_json(orient='records', force_ascii=False)
        connection.close()
        
        user = sys_user.query.get("LTS")
        print(user.CREATE_TIME)
        print(df_json)
        return json.loads(df_json)
    
    def getSysUserById(id):
        getUser = db.get_or_404(sys_user, id)
        print(getUser.USER_ID)
        print(getUser.PASSWORD)
        print(getUser.CREATE_TIME)
        # jsonifyGet = jsonify(getUser)

        if getUser.CREATE_TIME :
            getUser.CREATE_TIME = datetime.datetime.strftime(getUser.CREATE_TIME, "%Y/%m/%d %H:%M:%S")
        if getUser.UPDATE_TIME :
            getUser.UPDATE_TIME = datetime.datetime.strftime(getUser.UPDATE_TIME, "%Y/%m/%d %H:%M:%S")

        getUser_dict = as_dict(getUser)

        return getUser_dict
    
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

        try:
            db.session.add(user)
            db.session.commit()

            return {'message': 'User added successfully'}, 200
        except DataError as e:
            db.session.rollback()
            print(e)
            # Return an error response with HTTP status code 409 Conflict
            return {'error': 'Username already exists'}, 409
        except Exception as e:
            print(e)
            # Handle other unexpected errors
            db.session.rollback()

            # Return an error response with HTTP status code 500 Internal Server Error
            return {'error': 'An error occurred'}, 500

    def modifySysUser(data):
        current = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        try:
            # user = sys_user.query.filter_by(USER_ID=data['USER_ID']).one()
            user = sys_user.query.filter_by(USER_ID=data['USER_ID']).first_or_404(description=f"There is no data with {data['USER_ID']}")
            user.USER_NAME="been change"
            user.UPDATE_TIME=current
            db.session.commit()
            return {"message": "update successed"}
        except Exception as e:
            print(e)
            return {"message":f"{e}"}

    def delSysUser(data):
        try:
            sys_user.query.filter_by(USER_ID=data['USER_ID']).delete()
            db.session.commit()
            return {"message": f"{data['USER_ID']} has been delete"}
        except Exception as e:
            print(e)
            return {"message":f"{e}"}

    def validate(data):
        print(data)
        print(type(data))
        print(data['USER_ID'])
        print(type(data['USER_ID']))

        beforeMd5 = data['USER_ID']+data['PASSWORD']

        connection = engine.connect()

        df = pd.read_sql(text(f"select * from sys_user where USER_ID='{data['USER_ID']}'"), connection)

        # Convert a specific column to string
        df['CREATE_TIME'] = df['CREATE_TIME'].astype(str)
        df['UPDATE_TIME'] = df['UPDATE_TIME'].astype(str)

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
    