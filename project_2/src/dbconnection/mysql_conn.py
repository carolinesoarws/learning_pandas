import pymysql
import mysql.connector
from sqlalchemy import create_engine


def creating_connection_mysql():
    engine = str
    print("Creating connection with Mysql")
    host = 'db-test.c5drx2ef5eqh.us-east-1.rds.amazonaws.com'
    port = 3306
    user = 'carol'
    password = 'password'
    database = 'mydbtest'

    print(f"Mysql connection info: host: {host}, "
          f"port: {port}, "
          f"user: {user}")
    # Connect to the database
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        conn.commit()

        print("Creating Engine to connect to create DataFrame")
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    except ConnectionError as exp:
        print(f"Connection error: {exp}")

    return engine
