import pyodbc

conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                      SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

cur = conn.cursor()

id = input('Enter id for update: ')
name = input('Enter name: ')

cur.execute('update Training.dbo.Customer set Cust_Name=? where CustomerID=?', (name, id))

cur.commit()

conn.close()
