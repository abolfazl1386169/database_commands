import sqlite3
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
table = '''CREATE TABLE users(
        name_food VARCHAR(255) NOT NULL ,  
        type VARCHAR(255) NOT NULL ,
        price VARCHAR(255) NOT NULL , 
        number VARCHAR(255) NOT NULL ,
        sum_price VARCHAR(255) NOT NULL ,
        time_left VARCHAR(255) NOT NULL  
);'''
cursor.execute(table)
conn.commit()
conn.close()
print("secsesful")