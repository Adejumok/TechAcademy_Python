from tkinter import *
from db_connect import DB


class GUI:
    def __init__(self, db):
        self.db = db

        self.top = Tk()

        # ID Entry
        self.id_label = Label(self.top, text='ID')
        self.id_label.grid(row=0, column=0)

        self.var_id = StringVar()
        self.id_entry = Entry(self.top, bd=5, textvariable=self.var_id)
        self.id_entry.grid(row=0, column=1)

        # Name Entry
        self.name_label = Label(self.top, text='Name')
        self.name_label.grid(row=1, column=0)

        self.var_name = StringVar()
        self.name_entry = Entry(self.top, bd=5, textvariable=self.var_name)
        self.name_entry.grid(row=1, column=1)

        # Address Entry
        self.address_label = Label(self.top, text='Address')
        self.address_label.grid(row=2, column=0)

        self.var_address = StringVar()
        self.address_entry = Entry(self.top, bd=5, textvariable=self.var_address)
        self.address_entry.grid(row=2, column=1)

        # Create Button
        self.create_button = Button(self.top, text="Create", command=self.create_record)
        self.create_button.grid(row=3, column=0, padx=10, pady=10)

        # Update Button
        self.update_button = Button(self.top, text="Update", command=self.update_record)
        self.update_button.grid(row=3, column=1, padx=10, pady=10)

        # Delete Button
        self.delete_button = Button(self.top, text="Delete", command=self.delete_record)
        self.delete_button.grid(row=4, column=0, padx=10, pady=10)

        # Display Button
        self.display_button = Button(self.top, text="Display", command=self.display_all_records)
        self.display_button.grid(row=4, column=1, padx=10, pady=10)

        # Display by ID Button
        self.display_id_button = Button(self.top, text="Display by ID", command=self.display_record_by_id)
        self.display_id_button.grid(row=4, column=2, padx=10, pady=10)

        self.exit_button = Button(text="Exit", command=self.top.destroy)
        self.exit_button.grid(row=0, column=2, padx=10, pady=10)

        self.top.mainloop()

    def handle_button(self, operation):
        if operation == "Create":
            name = self.var_name.get()
            address = self.var_address.get()

            try:
                self.db.create_record(name, address)
            except Exception as e:
                print("Exception occurred during create operation:", e)

        elif operation == "Update":
            id = self.var_id.get()
            name = self.var_name.get()
            address = self.var_address.get()

            try:
                self.db.update_record(id, name, address)
            except Exception as e:
                print("Exception occurred during update operation:", e)


        elif operation == "Display":
            try:
                self.db.display_all_records()
            except Exception as e:
                print("Exception occurred during display operation:", e)

        elif operation == "Display by ID":
            id = self.var_id.get()

            try:
                self.db.display_record_by_id(id)
            except Exception as e:
                print("Exception occurred during display by ID operation:", e)

    def create_record(self):
        self.handle_button("Create")

    def update_record(self):
        self.handle_button("Update")

    def delete_record(self):
        self.handle_button("Delete")

    def display_all_records(self):
        self.handle_button("Display")

    def display_record_by_id(self):
        self.handle_button("Display by ID")


server = "ISW-220521-608\SQLEXPRESS"

db = DB(server)
db.connect()

gui = GUI(db)

db.disconnect()
