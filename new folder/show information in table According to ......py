import sqlite3
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
x = cursor.execute("SELECT * FROM ALI ORDER BY city")
for i in x :
    print(i)
conn.commit()
conn.close()