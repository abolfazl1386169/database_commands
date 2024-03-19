import sqlite3
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
cursor.execute('''UPDATE ALI SET 'city' = 'ali' WHERE city = 'norbakhsh' ;''')
conn.commit()
conn.close()
