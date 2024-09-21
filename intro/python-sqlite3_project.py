import sqlite3
connect = sqlite3.connect("Cry of Fear.db")
cursor = connect.cursor()
cursor.execute('''create table if not exists Cry_of_Fear(Player_name varchar(255), Chapters_completed int)''')
cursor.execute('''insert into Cry_of_Fear(Player_name, Chapters_completed) values('Darsh', 3)''')
cursor.execute('''insert into Cry_of_Fear(Player_name, Chapters_completed) values('Akash sir', 4)''')
connect.commit()
cursor.execute('''select * from Cry_of_Fear''')

#list
List = cursor.fetchall()
for x in List:
    print(x)