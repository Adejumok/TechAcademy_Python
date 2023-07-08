import pyodbc

conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                      SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

cur = conn.cursor()

id = input('Enter id: ')
name = input('Enter name: ')
city = input('Enter city: ')
grade = input('Enter grade: ')
salesManId = input('Enter SalesManId: ')

cur.execute('insert into Training.dbo.Customer values(?, ?, ?, ?, ?)', (id, name, city, grade, salesManId))

cur.commit()

conn.close()
