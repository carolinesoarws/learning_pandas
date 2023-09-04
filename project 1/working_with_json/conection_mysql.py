import pymysql
import mysql.connector
from sqlalchemy import create_engine


def mysql_connection():
    host = 'db-test.c5drx2ef5eqh.us-east-1.rds.amazonaws.com'
    port = 3306
    user = 'carol'
    password = 'password'
    database = 'mydbtest'

    # Connect to the database
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    conn.commit()

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine
