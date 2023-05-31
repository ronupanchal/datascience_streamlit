import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Omsairam@257016",
)

print(mydb)

mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE mydatabase")