import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

def configure_db(db):
    if db == "sqlite":
        db_file_path = os.getenv("sqlite_db_file")
        configure_sqlite_db(db_file_path)

def configure_sqlite_db(db_file_path):
    conn = sqlite3.connect(db_file_path)
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    #create required tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages 
                    (id INTEGER PRIMARY KEY,
                    type TEXT NOT NULL,
                    recipient TEXT NOT NULL,
                    message_content TEXT NOT NULL,
                    status_code TEXT,
                    timestamp INTEGER)'''
                )
    cursor.execute('''CREATE TABLE IF NOT EXISTS message_status 
                    (msg_id INTEGER PRIMARY KEY ASC,
                    status  TEXT ,
                    timestamp INTEGER )'''
                                 ) 

    # Save the changes and close connection
    conn.commit()
    conn.close()

def sqlite_connection(db_file_path,QUERY,DATA=None):
    configure_sqlite_db(db_file_path)
    if DATA is None:
        DATA = ()
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute(QUERY, DATA)
    conn.commit()
    conn.close()

def insert_data(db_file_path,table,columns, data):
    val = ", ".join(["?" for c in columns])
    col = ", ".join(columns)
    query = f'''INSERT INTO {table}({col}) VALUES ({val})'''
    sqlite_connection(db_file_path,query, data)

def get_all_data(db_file_path,table):
    configure_sqlite_db(db_file_path)

    query = f"SELECT * FROM {table}"

    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()

    return data
    