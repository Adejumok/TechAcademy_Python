import pyodbc

try:
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;\
                      SERVER=ISW-220521-608\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    sql='insert into Training.dbo.Academy values(?, ?, ?)'
    records=[(1, 'John', 45500), (2, 'Jummy', 67500), (3, 'Eben', 10000)]
    cur.executemany(sql, records)
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

