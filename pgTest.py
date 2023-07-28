import pandas as pd
import sqlalchemy
from sqlalchemy import text

# build engine from sqlalchemy
engine = sqlalchemy.create_engine(
    f'postgresql://postgres:PassW0rd@172.26.0.4:5432/mma')

connection = engine.connect()

# df = pd.read_sql(text("select upd_date_time, process_id from master_temp;"), connection)
df = pd.read_sql(text("select * from district_office;"), connection)

df_json = df.to_json(orient='records', force_ascii=False)
connection.close()

print(df)