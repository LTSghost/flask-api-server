import os
from dotenv import load_dotenv

load_dotenv()

# 連線 MYSQL
username = os.environ.get("MYSQL_USERNAME")  # 資料庫帳號
password = os.environ.get("MYSQL_PASSWORD")  # 資料庫密碼
host = os.environ.get("MYSQL_DB_ADDRESS")    # 資料庫位址
port = os.environ.get("MYSQL_PORT")          # 資料庫埠號
database = os.environ.get("MYSQL_DB")        # 資料庫名稱

server_port = os.environ.get("SERVER_PORT")