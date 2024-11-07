import os
import psycopg2
from dotenv import load_dotenv

import sqlite3
load_dotenv()


def db_connection(QUERY,DATA):
    conn = psycopg2.connect(host="localhost",
            database= os.getenv("DATABASE"),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD')) 
    cur = conn.cursor() 
    cur.execute(QUERY,DATA) 
    # data = cur.fetchall()
    conn.commit() 
    cur.close() 
    conn.close() 

def sqlite_connection(QUERY,DATA):
    db_file_path = os.getenv("sqlite_db_file")
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute(QUERY, DATA)
    conn.commit()
    conn.close()
