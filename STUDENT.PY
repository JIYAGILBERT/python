import sqlite3
conn=sqlite3.connect('mydb.db')
cursor=conn.cursor()

# cursor.execute("CREATE TABLE STUDENT(ID text,NAME text,AGE text,GRADE text, CITY text )")

# data=[('1','sandra','20','A+','ERNAKULAM'),
#       ('2','Abdhulla','21','B+','ALUVA'),
#       ('3','Athul','22','C+','ALAPUZHA'),
#       ('4','ANNIT','18','D+','KOTTAYAM'),
#       ('5','RAHUL','25','E+','IDUKKI'),
#       ]
# cursor.executemany("INSERT INTO STUDENT (ID, NAME,AGE,GRADE,CITY) VALUES (?, ?, ?, ?, ?)", data)
# conn.commit()
# conn.close()
# print("data inserted")


# p=cursor.execute("UPDATE STUDENT SET  Name = 'JEFFIN' WHERE ID=3 ")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

p=cursor.execute("DELETE FROM STUDENT WHERE ID = 1 ")
for i in p:
    print(i)
conn.commit()
conn.close()