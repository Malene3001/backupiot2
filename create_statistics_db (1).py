import sqlite3 as sql

con = sql.connect('db_statistics.db')

cur = con.cursor()

sql = '''CREATE TABLE "Temperature & Humidity" (
"Temperature"  INTEGER PRIMARY KEY AUTOINCREMENT,
"Humidity" TEXT,
"Time" TEXT
)'''

cur.execute(sql)

con.commit()

print("Table created, successfully")

con.close()