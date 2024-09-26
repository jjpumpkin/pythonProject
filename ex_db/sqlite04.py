import sqlite3
conn =sqlite3.connect('mydb.db')
sql = """
     SELECT *
     FROM stocks
"""
cur = conn.cursor()
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(row)
    conn.close()