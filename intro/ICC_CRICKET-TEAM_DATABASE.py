import sqlite3
connect = sqlite3.connect("Cricket_Team.db")
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Cricket_Team(Player_name varchar(255), Role varchar(255), Age int)''')
numberOfRecords = int(input("How many players are there in your team?"))
ListofTuples = []
for x in range(numberOfRecords):
    Player_name = input("What is the player's name?")
    Role = input("What is the role of the player?")
    Age = input("What is the age of the player?")
    tuple = (Player_name, Role, Age)
    ListofTuples.append(tuple)
cursor.executemany('''INSERT INTO Cricket_Team(Player_name,Role,Age) Values(?,?,?)''',ListofTuples)
#display on sqlite3
cursor.execute('''SELECT * FROM Cricket_Team''')
connect.commit()
#display on py
List = cursor.fetchall()
for x in List:
    print(x)