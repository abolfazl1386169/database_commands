import sqlite3
conn = sqlite3.connect('students_database.db')
corsor = conn.cursor()
list_name_food = ["egg","Chicken","Soup","sushi","Pizza"]
list_price_food = [10000,50000,40000,60000,80000]
list_number_food = [2,5,6,3,2]
list_time_food = [5,15,20,10,20]
for i in range(len(list_name_food)) :
    sum_price = list_number_food[i] * list_price_food[i] 
    corsor.execute('''INSERT INTO users (name_food, type, price, number, sum_price, time_left) VALUES (?, ?, ?, ?, ?, ?)''', (list_name_food[i],"food", list_price_food[i], list_number_food[i],sum_price,list_time_food[i]))
    sum_price = 1 
    print(f"number{i}add in table")
conn.commit()
conn.close()
print("first edit with github")
