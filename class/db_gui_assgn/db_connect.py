import pyodbc


class DB:
    def __init__(self, server):
        self.server = server
        self.connection = None
        self.cursor = None
        print('Connecting to SQLEXPRESS....')

    def connect(self):
        try:
            self.connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;\
                                   SERVER={self.server};DATABASE=Training;Trusted_Connection=yes;')
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully.")
        except pyodbc.Error as error:
            print("Error connecting to the database:", error)
            self.connection.rollback()
            raise

    def create_record(self, name, address):
        try:
            self.cursor.execute("INSERT INTO Training.dbo.Interswitch (Name, Address) VALUES (?, ?)", name, address)
            self.connection.commit()
            print("Record created successfully")
        except pyodbc.Error as e:
            print("Error creating record:", e)
            self.connection.rollback()
            raise

    def update_record(self, id, name, address):
        try:
            self.cursor.execute("UPDATE Training.dbo.Interswitch SET Name=?, Address=? WHERE ID=?", name, address, id)
            self.connection.commit()
            print("Record updated successfully")
        except pyodbc.Error as e:
            print("Error updating record:", e)
            self.connection.rollback()
            raise

    def display_all_records(self):
        try:
            self.cursor.execute("SELECT * FROM Training.dbo.Interswitch")
            rows = self.cursor.fetchall()

            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Error displaying records:", e)
            raise

    def display_record_by_id(self, id):
        try:
            self.cursor.execute("SELECT * FROM Training.dbo.Interswitch WHERE ID=?", id)
            row = self.cursor.fetchone()

            if row:
                print(row)
            else:
                print("Record not found")
        except pyodbc.Error as e:
            print("Error displaying record by ID:", e)
            raise

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Disconnected from the database")

