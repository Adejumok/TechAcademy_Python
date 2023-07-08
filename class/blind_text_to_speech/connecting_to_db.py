import pyodbc


class Database:
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

    def create_table(self, table_name, columns):
        try:
            create_table_query = f"CREATE TABLE {table_name} ({columns})"
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print(f"Table '{table_name}' created successfully.")
        except pyodbc.Error as error:
            print("Error creating table:", error)
            self.connection.rollback()
            raise

    def insert_data(self, table_name, data):
        try:
            insert_query = f"INSERT INTO {table_name} VALUES ({data})"
            self.cursor.execute(insert_query)
            self.connection.commit()
            print("Data inserted successfully.")
        except pyodbc.Error as error:
            print("Error inserting data:", error)
            self.connection.rollback()
            raise

    def read_data(self, table_name):
        try:
            select_query = f"SELECT * FROM {table_name}"
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            print(f"Data from table '{table_name}':")
            for row in rows:
                print(row)
        except pyodbc.Error as error:
            print("Error reading data:", error)
            self.connection.rollback()
            raise

    def read_data_with_name(self, name, table_name):
        try:
            select_query = f"SELECT * FROM {table_name} WHERE Name = '{name}'"
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            print(f"Data from table '{table_name}':")
            for row in rows:
                print(row)
        except pyodbc.Error as error:
            print("Error reading data:", error)
            self.connection.rollback()
            raise

    def delete_data(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition}"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print("Data deleted successfully.")
        except pyodbc.Error as error:
            print("Error deleting data:", error)
            self.connection.rollback()
            raise

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Disconnected from the database")


# Example usage
db = Database("ISW-220521-608\SQLEXPRESS")

db.connect()

db.create_table("Training.dbo.BlindP_Name_Email", "id INTEGER PRIMARY KEY, name varchar(25), email varchar(45)")
db.create_table("Training.dbo.BlindP_Email_Message", "id INTEGER PRIMARY KEY, email varchar(45), name varchar(25)")


db.insert_data("Training.dbo.BlindP_Name_Email", "1, 'Tayo', 'tayo@gmail.com'")
db.insert_data("Training.dbo.BlindP_Name_Email", "2, 'Nana', 'omma@gmail.com'")
db.insert_data("Training.dbo.BlindP_Name_Email", "3, 'Uyoz', 'uyoz@gmail.com'")
db.insert_data("Training.dbo.BlindP_Name_Email", "4, 'Topa', 'outofoffice@gmail.com'")
db.insert_data("Training.dbo.BlindP_Name_Email", "5, 'John', 'ade@gmail.com'")
db.insert_data("Training.dbo.BlindP_Name_Email", "6, 'Ima', 'fk@gmail.com'")

db.read_data("Training.dbo.BlindP_Name_Email")

db.delete_data("Training.dbo.BlindP_Name_Email", "id = 5")

db.read_data("Training.dbo.BlindP_Name_Email")

db.read_data_with_name("Tayo", "Training.dbo.BlindP_Name_Email")

db.disconnect()
