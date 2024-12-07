import sqlite3
conn=sqlite3.connect('mydb.db')
cursor=conn.cursor()

# cursor.execute("CREATE TABLE STUDENT(ROLLNO text, Name text)")

data=[('2','sandra'),('3','Abdhulla'),('4','Athul')]
cursor.executemany("INSERT INTO STUDENT (ROLLNO, Name) VALUES (?, ?)", data)
conn.commit()
conn.close()
print("data inserted")