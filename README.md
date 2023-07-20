# Flask-API-server (Flask-RESTX)
- [開發環境](#開發環境)
- [專案結構](#專案結構)

## 開發環境
\* requirement : python 3.7+
### 佈署與建置

#### 建立 .venv
```
python3 -m venv .venv
```
#### 下載套件
```python
pip3 install -r requirements.txt
```
#### 新增 .env 設定環境
nano .env
```
MYSQL_USERNAME=root
MYSQL_PASSWORD=password
MYSQL_DB_ADDRESS=localhost
MYSQL_PORT=3306
MYSQL_DB=db_name
...
```
### 專案結構
```txt
project/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── ...
│   ├── routes/
│   │   ├── __init__.py (initial swagger routes, and register into routes from others .py file)
│   │   ├── user.py
│   │   └── ...
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── ...
│   ├── static/
│   ├── templates/
│   └── utils/
│       ├── __init__.py
│       ├── authentication.py
│       └── ...
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   └── ...
├── config.py (get value from system)
├── requirements.txt
└── run.py
```