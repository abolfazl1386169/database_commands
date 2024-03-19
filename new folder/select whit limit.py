# importing sqlite module 
import sqlite3 

# create connection to the database 
# geeks_database 
connection = sqlite3.connect('geeks_database.db') 

# sql query to display top4 data from table 
cursor = connection.execute("SELECT * FROM customer_address LIMIT 4") 

# display data row by row 
for i in cursor: 
	print(i) 

# close the connection 
connection.close() 
