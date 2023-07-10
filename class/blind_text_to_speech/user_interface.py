from tkinter import *

import tkinter.messagebox




class Database_Frame(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)

        self.master = master

        self.pack(fill=BOTH, expand=1)




        # Button to send email at bottom left of frame

        self.send_mail = Button(self, text="Send", command=self.send_email)

        self.send_mail.place(x=400, y=550)




        # Button to exit program at bottom right of frame

        self.exit_button = Button(self, text="Exit", command=self.exit_program)

        self.exit_button.place(x=500, y=550)




    def send_email(self):

        send = tkinter.messagebox.askyesno("Send", "Are you sure you want to send this email?")

        if send > 0:

            return tkinter.messagebox.showinfo("SENT", "Email sent successfully!")





    def exit_program(self):

        exit()




root = Tk()

root.title("Database")

root.geometry("600x600")

root.resizable(False, False)




app = Database_Frame(root)




email_label = Label(app, text="Email: ")

email_label.place(x=0, y=0)




email_entry = Entry(app)

email_entry.place(x=50, y=0)




subject_label = Label(app, text="Subject: ")

subject_label.place(x=0, y=30)




subject_entry = Entry(app)

subject_entry.place(x=50, y=30)




message_label = Label(app, text="Message: ")

message_label.place(x=0, y=60)




message_text = Text(app, height=10, width=50)

message_text.place(x=44, y=90)




root.mainloop()