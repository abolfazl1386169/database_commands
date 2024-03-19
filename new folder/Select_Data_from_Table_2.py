import sqlite3
import time
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
read_row = '''SELECT * FROM ALI'''
cursor.execute(read_row)
print("read information is secsesful!!")
output = cursor.fetchmany(5) 
for row in output :
    print(row)
    print(30*"-")
    time.sleep(2)
conn.commit()
conn.close()
