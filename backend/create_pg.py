import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='nitin$11122',
    host='localhost'
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute('DROP DATABASE IF EXISTS varuna;')
cur.execute('CREATE DATABASE varuna;')
cur.close()
conn.close()
print('Database varuna created!')
