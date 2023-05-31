import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Omsairam@257016",
  database="mydatabase"
)

mycursor = mydb.cursor()

#create new table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)