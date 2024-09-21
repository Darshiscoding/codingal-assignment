import sqlite3
connect = sqlite3.connect("Employee.db")
cursor = connect.cursor()
cursor.execute('''create table if not exists Employee(name varchar(255), age int, salary int)''')
cursor.execute('''insert into Employee(name,age,salary) values('Rohit', 35, 40000)''')
cursor.execute('''insert into Employee(name,age,salary) values('Keshav', 24, 70000)''')
connect.commit()
cursor.execute('''select * from Employee''')
list = cursor.fetchall()
for x in list:
    print(x)