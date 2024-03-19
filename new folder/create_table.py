import sqlite3
connection_obj = sqlite3.connect('students_database.db')
cursor_obj = connection_obj.cursor()
table = '''CREATE TABLE ALI(
        name VARCHAR(255) NOT NULL ,  
        phone_number VARCHAR(255) NOT NULL,
        number VARCHAR(255) NOT NULL ,
        code_male VARCHAR(255) NOT NULL 
);'''
cursor_obj.execute(table)
print("secsesful!!")
connection_obj.close()
