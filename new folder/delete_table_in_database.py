import sqlite3
connection_obj = sqlite3.connect('students_database.db')
cursor = connection_obj.cursor()
cursor.execute("DROP TABLE IF EXISTS aby")
print("secsesful!!")
connection_obj.close()