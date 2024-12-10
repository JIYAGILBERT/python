import mysql.connector

connection=mysql.connector.Connect(
    host="localhost",
    user="gilbert",
    password="gilbert0987",
    database="mydb"
)
print("connected successfully")
connection.close()











