import sqlite3
connect = sqlite3.connect("Employee.db")
cursor = connect.cursor()
cursor.execute('''CREATE TABLE if not exists Employee(Name varchar(255), salary int)''')

cursor.execute('''DELETE FROM Employee''')

# we will create 2 variables name and salary then we will take the input from user

#
listOfTuples = [("A",4),("B",3),("C",5),("D",6),("F",8),("Z",76)]
# insert
cursor.executemany('''INSERT INTO Employee(Name, salary) VALUES(?,?)''',listOfTuples)   

connect.commit()
cursor.execute('''SELECT * FROM Employee''')   
 
List = cursor.fetchall()
for x in List:
     print(x)

