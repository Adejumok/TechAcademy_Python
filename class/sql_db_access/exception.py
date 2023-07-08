import pyodbc

try:
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                      SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    cur.execute('create table Training.dbo.Good(stu_no int, stu_name varchar(10), stu_all decimal(10,2))')
    print('Successful!')
    conn.commit()

except pyodbc.Error as e:
    if conn:
        conn.rollback()
        print(e)
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()

