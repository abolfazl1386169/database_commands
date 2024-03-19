import sqlite3
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()
show_information =  cursor.execute("SELECT * FROM users ORDER BY name_food ")
x = 0
Order_list = []
print("'name_food' ,'type' ,'price' ,'number' ,'sum_price' ,'time_left'")
for i in show_information :
    Order_list.insert(x,i)
    print(Order_list[x])
    x += 1
conn.commit()
conn.close()