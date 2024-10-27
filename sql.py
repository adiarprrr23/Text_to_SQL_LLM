import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""

    Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)

"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Aditya','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Rohan','Data Science','A',85)''')
cursor.execute('''Insert Into STUDENT values('Likith','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Shreyas','Devops','A',95)''')
cursor.execute('''Insert Into STUDENT values('Prajwal','Devops','A',90)''')

print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()