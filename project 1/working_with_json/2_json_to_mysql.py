import pandas as pd
import json
from conection_mysql import mysql_connection

# reading a json file
mydata = open("example_2.json", "r").read()

# loading the file into a json
mydata = json.loads(mydata)
print(mydata)

# Turning my json into a dataframe
mydf = pd.json_normalize(mydata, record_path="Candidates")
print(mydf.to_string())

# validating if the is duplicated data
# Removing the duplicated data
print(mydf.duplicated())
mydf.drop_duplicates(inplace=True)
print(mydf)

# validating null values into dataframe
print(mydf.isnull().values.any())
print(mydf.isnull().sum())

# Removing the null values
mydf["age"].fillna(0, inplace=True)
mydf["hobby.gaming"].fillna(0, inplace=True)
mydf["hobby.reading"].fillna("True", inplace=True)
print(mydf)
print(mydf.to_string())

# Connecting to mysql and creating the table with the values
engine = mysql_connection()
mydf.to_sql(con=engine, name='candidates', if_exists='append', index=False)

print(mydf)
