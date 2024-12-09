import sqlite3
conn=sqlite3.connect('mydb.db')
cursor=conn.cursor()

# cursor.execute("CREATE TABLE STUDENT(ROLLNO text, Name text)")

# data=[('2','sandra'),('3','Abdhulla'),('4','Athul')]
# cursor.executemany("INSERT INTO STUDENT (ROLLNO, Name) VALUES (?, ?)", data)
# conn.commit()
# conn.close()
# print("data inserted")

# p=cursor.execute("SELECT * FROM STUDENT")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()


# p=cursor.execute("SELECT Name FROM STUDENT ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT * FROM STUDENT WHERE ROLLNO>2 ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("UPDATE STUDENT SET  Name = 'RAHUL' WHERE ROLLNO=2 ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("DELETE FROM STUDENT WHERE ROLLNO = 4  ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()


# p=cursor.execute("SELECT MAX(ROLLNO) FROM STUDENT  ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()


# p=cursor.execute("SELECT MIN(ROLLNO) FROM STUDENT ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# SAME NAME 

# p=cursor.execute("SELECT NAME,COUNT(*) FROM STUDENT GROUP BY NAME ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("DROP TABLE STUDENT ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()