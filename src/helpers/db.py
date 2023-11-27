import psycopg2
import random


conn = psycopg2.connect(
    database='mydb',
    user='u0_a454',
    password='8871745412',
    host='0.tcp.in.ngrok.io',
    port=16864

)


cur = conn.cursor()
