import sqlite3 as sql

conn = sql.connect(':memory:') # connect or create database file
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

conn.close()