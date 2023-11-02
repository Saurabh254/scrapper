import psycopg2
import random


conn = psycopg2.connect(
    database='mydb',
    user='postgres',
    password='12345678',
)


cur = conn.cursor()

cur.execute(f"INSERT INTO some_table (x, y) VALUES {2, 3}")
conn.commit()
