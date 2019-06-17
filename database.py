import sqlite3


conn = sqlite3.connect('hack_db')
cur = conn.cursor()
cur.execute("DELETE FROM HackData WHERE registration_no='null'")
s = cur.fetchall()
conn.commit()
print(s)
