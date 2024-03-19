import sqlite3
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM ALI WHERE name = 'ali' ")
conn.commit()
conn.close()
