import sqlite3 as sql

conn = sql.connect(':memory:') # connect or create database
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Track (title, plays) VALUES (?,?)',
            ('Thunderstrck', 20))
cur.execute('INSERT INTO Track (title, plays) VALUES (?,?)',
            ('My Way', 15))
conn.commit()

print('Track:')
cur.execute('SELECT * FROM Track')
for row in cur:
    print(row)

cur.execute('DELETE FROM Track WHERE plays < 100')
conn.commit()

conn.close()