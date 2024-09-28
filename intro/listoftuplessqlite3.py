import sqlite3
connect = sqlite3.connect("Student_marks.db")
cursor = connect.cursor()
cursor.execute('''CREATE TABLE if not exists Student_marks(name varchar(255), class int, marks int)''')
cursor.execute('''DELETE FROM Student_marks''')
numberOfRecords = int(input("How many records do you want to enter?"))
Listoftuples =  []
for x in range(numberOfRecords):
    name = input("Enter name of student: ")
    class_student = input("Enter class of student: ")
    marks = input("Enter marks of student: ")
    tuple = (name,class_student,marks)
    Listoftuples.append(tuple)
cursor.executemany('''INSERT INTO Student_marks(name,class,marks) VALUES(?,?,?)''',Listoftuples)
connect.commit()
cursor.execute('''SELECT * FROM Student_marks''')
list = cursor.fetchall()
for x in list:
    print(x)