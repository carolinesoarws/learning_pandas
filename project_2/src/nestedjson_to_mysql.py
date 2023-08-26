import pandas as pd
import json
from dbconnection import mysql_conn

with open('data.json') as f:
    data = json.load(f)
    
df = pd.json_normalize(data, record_path=["books"])
print(df.to_string())

# inserting to mysql
engine = mysql_conn.creating_connection_mysql()
return_code = df.to_sql(name="books", con=engine, if_exists='append', index=False)
print(return_code)
