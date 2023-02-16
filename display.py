import sqlite3
conn=sqlite3.connect('Mid-morning.db')
data=conn.execute("select  *  from Students")
for row in data:
    print("ID=", row[0])
    print("NAME=", row[1])
    print("AGE=", row[2])
    print("SCHOOL=", row[3])
    print("GENDER=", row[4],"\n")
conn.close()