import sqlite3 as sql

conn = sql.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM armory_item;'
curs.execute(query).fetchall()