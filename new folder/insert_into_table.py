import sqlite3
connection_obj = sqlite3.connect('students_database.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute('''INSERT INTO ALI (name) VALUES ('ali')''')
print("Data Inserted in the table: ")
data=cursor_obj.execute('''SELECT * FROM ALI''') 
for row in data: 
    print(row) 
connection_obj.commit()
connection_obj.close()