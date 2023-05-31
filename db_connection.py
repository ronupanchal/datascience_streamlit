import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Omsairam@257016",
    database="mydb"
)

print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO tbl_std (sid, sname) VALUES (%s, %s)"
val = (1, "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
