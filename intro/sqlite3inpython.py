import sqlite3
connect = sqlite3.connect()
cursor = connect.cursor()
cursor.execute('''CREATE TABLE Minecraft( Server_name varchar(255), username varchar(255), kills int, deaths int)''')
cursor.execute('''INSERT INTO Minecraft(Server_name,username,kills,deaths) VALUES('HAIDER_NET', 'Darsh_MC', 500, 24)''')
cursor.execute('''INSERT INTO Minecraft(Server_name,username,kills,deaths) VALUES('HAIDER_NET', 'Robert#1234', 125, 27)''')
cursor.execute('''SELECT * FROM Minecraft''')

List = cursor.fetchall()
for x in List:
    print(x)