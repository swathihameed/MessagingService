import os
import psycopg2
from dotenv import load_dotenv


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