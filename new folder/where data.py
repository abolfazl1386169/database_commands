import sqlite3
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM ALI WHERE name = 'ali' ")
print(cursor.fetchall())
conn.commit()
conn.close()
