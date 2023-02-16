import sqlite3
conn=sqlite3.connect('Mid-morning.db')
print("open database successfully")
conn.execute("CREATE TABLE Students("
             "ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("table created successfully")
conn.close()