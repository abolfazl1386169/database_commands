import sqlite3
connection_obj = sqlite3.connect('students_database.db')
cursor_obj = connection_obj.cursor()
s = ["hoshang","javad","hossen","abolfazl","parsa","hamid","saed","reza","mmd","ali"]
y = ["09138902542","09130122546","09027452546","09027481521","09165486598","09011234567","09012345678","09005264357","09324569875","09001234568"]
w = ["20","14","13","12","11","10","15","16","14","18"]
v = ["6200141842","6209795020","6200145889","6200132546","6200145235","6200215263","6203653578","6201589263","6202542126","6200121258"]

for i in range(len(s)):
    cursor_obj.execute('''INSERT INTO ALI (name, phone_number, number, code_male) VALUES (?, ?, ?, ?)''', (s[i], y[i], w[i], v[i]))

connection_obj.commit()
connection_obj.close()