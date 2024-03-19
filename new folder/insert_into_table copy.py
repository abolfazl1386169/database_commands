import sqlite3
connection_obj = sqlite3.connect('students_database.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute(
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk1@gmail.com","Geek1",25)''') 
cursor_obj.execute( 
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk2@gmail.com","Geek2",15)''') 
cursor_obj.execute( 
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk3@gmail.com","Geek3",36)''') 
cursor_obj.execute( 
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk4@gmail.com","Geek4",27)''') 
cursor_obj.execute( 
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk5@gmail.com","Geek5",40)''') 
cursor_obj.execute( 
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk6@gmail.com","Geek6",36)''') 
cursor_obj.execute( 
    '''INSERT INTO ALI (name,first_name,city) VALUES ("geekk7@gmail.com","Geek7",27)''') 
print("Data Inserted in the table: ")
data=cursor_obj.execute('''SELECT * FROM ALI''') 
for row in data: 
    print(row) 
connection_obj.commit()
connection_obj.close()