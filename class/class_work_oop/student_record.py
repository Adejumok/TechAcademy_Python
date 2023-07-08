import pyodbc


class Student:

    def __init__(self):
        print('Welcome Student')

    # def create_table(self):
    #     try:
    #         conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
    #                               SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    #         cur = conn.cursor()
    #         cur.execute('create table Training.dbo.Student(id int primary key, name varchar(25), course_code varchar(10), mark decimal(10,2), grade char, employment_status varchar(25))')
    #         print('Successful!')
    #         conn.commit()
    #
    #     except pyodbc.Error as e:
    #         if conn:
    #             conn.rollback()
    #             print(e)
    #     finally:
    #         if cur:
    #             cur.close()
    #         if conn:
    #             conn.close()

    # def stu_details(self):
    #     try:
    #         conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
    #                               SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    #         cur = conn.cursor()
    #         id = 0
    #         while True:
    #             id += 1
    #             name = input('Enter name: ')
    #             print(""" Available Course Codes
    #             1. 001
    #             2. 002
    #             3. 003
    #             4. 004
    #             5. 005
    #             """)
    #             course_code = input('Enter course code: ')
    #             mark = float(input('Enter mark: '))
    #             grade = 'A'
    #             employment_status = None
    #             if 75 <= mark <= 100:
    #                 grade = 'A'
    #                 employment_status = 'Automatic Employment'
    #             elif 65 <= mark < 75:
    #                 grade='B'
    #                 employment_status ='Open to Work'
    #             elif 55 <= mark < 65:
    #                 grade='C'
    #                 employment_status='Open to Work'
    #             elif mark < 55:
    #                 grade='F'
    #                 employment_status= 'Probation'
    #             sql = "insert into Training.dbo.Student values(?, ?, ?, ?, ?, ?)"
    #             cur.execute(sql, (id, name, course_code, mark, grade, employment_status))
    #             print("Record Inserted Successfully")
    #             option = input("Do you want to insert one more record[Yes| No] :")
    #             if option == "No":
    #                 conn.commit()
    #                 break
    #     except pyodbc.Error as e:
    #         if conn:
    #             conn.rollback()
    #             print(e)
    #     finally:
    #         if cur:
    #             cur.close()
    #         if conn:
    #             conn.close()
    #

    def display_all_records(self):
        try:
            conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                              SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
            cur = conn.cursor()
            result = cur.execute('select * from Training.dbo.Student')
            for each in result:
                print(each)
                print()
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

    def display_probation(self):
        try:
            conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                              SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
            cur = conn.cursor()
            result = cur.execute("select * from Training.dbo.Student where employment_status = 'Probation'")
            for each in result:
                print(each)
                print()
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

    def display_automatic_emp(self):
        try:
            conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                              SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
            cur = conn.cursor()
            result = cur.execute("select * from Training.dbo.Student where employment_status = 'Automatic Employment'")
            for each in result:
                print(each)
                print()
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

    def display_open_to_work(self):
        try:
            conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                              SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
            cur = conn.cursor()
            result = cur.execute("select * from Training.dbo.Student where employment_status = 'Open to Work'")
            for each in result:
                print(each)
                print()
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


student = Student()
# student.create_table()
# student.stu_details()
# student.display_all_records()
student.display_probation()
student.display_automatic_emp()
student.display_open_to_work()
