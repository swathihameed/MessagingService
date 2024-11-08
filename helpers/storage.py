import os
import psycopg2
from dotenv import load_dotenv
import sqlite3

load_dotenv()

def configure_db(db):
    if db == "sqlite":
        db_file_path = os.getenv("sqlite_db_file")
        configure_sqlite_db(db_file_path)
    elif db == "psql":
        configure_psql_db()

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

def configure_psql_db():
    conn = psycopg2.connect(
            host="localhost",
            database= os.getenv("DATABASE"),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD')
            )
    
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS messages (msg_id serial PRIMARY KEY,
                                 type varchar (150) NOT NULL,
                                 recipient varchar (50) NOT NULL,
                                 message_content text NOT NULL,
                                 status_code varchar (50),
                                 timestamp date DEFAULT CURRENT_TIMESTAMP);'''
                                 )
    cur.execute('''CREATE TABLE IF NOT EXISTS message_status (msg_id serial PRIMARY KEY,
                                    status varchar (150) ,
                                    timestamp date );'''
                                    )
    
    conn.commit()

    cur.close()
    conn.close()

def psql_connection(QUERY,DATA):
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
    