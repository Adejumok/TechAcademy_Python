import pyodbc
try:
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                      SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    while True:
        stu_no=int(input("Enter Student Number: "))
        stu_name=input("Enter Student Name: ")
        stu_all=float(input("Enter Student Allowance: "))
        sql="insert into Training.dbo.Academy values(?, ?, ?)"
        cur.execute(sql,(stu_no, stu_name, stu_all))
        print("Record Inserted Successfully")
        option=input("Do you want to insert one more record[Yes| No] :")
        if option=="No":
            conn.commit()
            break
except pyodbc.Error as e:
    if conn:
        conn.rollback()
        print(e)
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()