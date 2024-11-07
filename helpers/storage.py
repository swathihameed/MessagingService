import os
import psycopg2
from dotenv import load_dotenv
import sqlite3

load_dotenv()

def configure_db(db):
    if db == "sqlite":
        configure_sqlite_db()
    elif db == "psql":
        configure_psql_db()

def configure_sqlite_db():
    db = "sqlite"
    db_file_path = os.getenv("sqlite_db_file")

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
                    (msg_id integer PRIMARY KEY ASC,
                    status  text ,
                    timestamp integer )'''
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

def sqlite_connection(QUERY,DATA):
    db_file_path = os.getenv("sqlite_db_file")
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute(QUERY, DATA)
    conn.commit()
    conn.close()
