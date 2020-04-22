import psycopg2
from config import *


def insert_data(value):
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASS, port=5432)
    except ConnectionError:
        return print("Unable to connect to database")
    cur = conn.cursor()
    cur.execute('INSERT INTO temperature (temperature, esp) VALUES(%s, %s)', (float(value), ))
    conn.commit()
    cur.close()
    conn.close()
    conn = None
    cur = None
    return "Success"

