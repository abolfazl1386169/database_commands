import sqlite3
connection_obj = sqlite3.connect('students_database.db')
cursor_obj = connection_obj.cursor()
table = '''CREATE TABLE users(
        username VARCHAR(255) NOT NULL ,  
        pasword VARCHAR(255) NOT NULL
);'''
cursor_obj.execute(table)
print("secsesful!!")
connection_obj.commit()
connection_obj.close()