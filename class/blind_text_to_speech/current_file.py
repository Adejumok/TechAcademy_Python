from connecting_to_db import *
from tkinter import *
import tkinter.messagebox
import smtplib
from email.mime.text import MIMEText
import speech_recognition as sr
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

        self.Myemail_label = Label(self, text="MyEmail: ")
        self.Myemail_label.place(x=0, y=0)
        self.Myemail_entry = Entry(self)
        self.Myemail_entry.place(x=58, y=0)
        self.Myemail = self.Myemail_entry.get()

        self.name_label = Label(self, text="Name: ")
        self.name_label.place(x=0, y=30)
        self.name_entry = Entry(self)
        self.name_entry.place(x=58, y=30)
        self.name_entry.config(validate="key", validatecommand=self.validate_name_entry)

        self.email_label = Label(self, text="Email: ")
        self.email_label.place(x=0, y=60)
        self.email_entry = Entry(self)
        self.email_entry.place(x=58, y=60)
        self.email = self.email_entry.get()

        self.subject_label = Label(self, text="Subject: ")
        self.subject_label.place(x=0, y=90)
        self.subject_entry = Entry(self)
        self.subject_entry.place(x=58, y=90)
        self.subject = self.subject_entry.get()

        self.message_label = Label(self, text="Message: ")
        self.message_label.place(x=0, y=120)
        self.message_text = Text(self, height=10, width=50)
        self.message_text.place(x=58, y=120)
        self.body = self.message_text.get("1.0", tkinter.END)

        self.password_label = Label(self, text="Password: ")
        self.password_label.place(x=0, y=300)
        self.password_entry = tkinter.Entry(self, show = '*', font = ('Arial', 14))
        self.password_entry.place(x = 58, y = 300)
        self.password = self.password_entry.get()

        # Initialize speech recognition
        self.r = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Button for speech recognition
        self.speech_button = Button(self, text="Speech Input", command=self.start_speech_recognition)
        self.speech_button.place(x=400, y=0)

        self.db_manager = Database()
        self.mainloop()
    
    def start_speech_recognition(self):
        try:
            with self.microphone as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)
                recognized_text = self.r.recognize_google(audio)
                self.populate_entries(recognized_text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

    def populate_entries(self, recognized_text):
        entries_data = recognized_text.split(';')
        for entry_data in entries_data:
            entry_type, entry_value = entry_data.split(':')
            if entry_type == "MyEmail":
                self.Myemail_entry.delete(0, END)
                self.Myemail_entry.insert(END, entry_value)
            elif entry_type == "Name":
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, entry_value)
            elif entry_type == "Email":
                self.email_entry.delete(0, END)
                self.email_entry.insert(END, entry_value)
            elif entry_type == "Subject":
                self.subject_entry.delete(0, END)
                self.subject_entry.insert(END, entry_value)
            elif entry_type == "Message":
                self.message_text.delete("1.0", END)
                self.message_text.insert("1.0", entry_value)
            elif entry_type == "Password":
                self.password_entry.delete(0, END)
                self.password_entry.insert(END, entry_value)

    def send_email(self):
        send = tkinter.messagebox.askyesno("Send", "Are you sure you want to send this email?")
        if send > 0:
            msg = MIMEText(self.body)
            msg['Subject'] = self.subject
            msg['From'] = self.Myemail
            msg['To'] = self.email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(self.Myemail, self.password)
                smtp_server.sendmail(self.Myemail, self.email, msg.as_string())
            print("Message sent!")
        return tkinter.messagebox.showinfo("SENT", "Email sent successfully!")
    
    def validate_name_entry(self):
        name = self.name_entry.get()

        # Call the database query method from the DatabaseManager instance
        rows = self.db_manager.read_data_with_name("email", name, 'BlindP_Name_Email')

        if rows:
            email = rows[0][0]
            self.email_entry.delete(0, tkinter.END)  # Clear any existing text in the email entry
            self.email_entry.insert(0, email)  # Set the retrieved email in the email entry
        else:
            self.email_entry.delete(0, tkinter.END)  # Clear the email entry if name not found

           
    def exit_program(self):
        exit()
    
    

root = Tk()

root.title("Database")

root.geometry("600x600")
root.resizable(False, False)
app = Database_Frame(root)
app