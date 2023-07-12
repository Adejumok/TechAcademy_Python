from tkinter import *

import tkinter.messagebox

import smtplib

from email.mime.text import MIMEText

import speech_recognition as sr


class DatabaseFrame(Frame):

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

        self.myemail_label = Label(self, text="MyEmail: ")

        self.myemail_label.place(x=0, y=0)

        self.myemail_entry = Entry(self)

        self.myemail_entry.place(x=58, y=0)

        self.name_label = Label(self, text="Name: ")

        self.name_label.place(x=0, y=30)

        self.name_entry = Entry(self)

        self.name_entry.place(x=58, y=30)

        self.email_label = Label(self, text="Email: ")

        self.email_label.place(x=0, y=60)

        self.email_entry = Entry(self)

        self.email_entry.place(x=58, y=60)

        self.subject_label = Label(self, text="Subject: ")

        self.subject_label.place(x=0, y=90)

        self.subject_entry = Entry(self)

        self.subject_entry.place(x=58, y=90)

        self.message_label = Label(self, text="Message: ")

        self.message_label.place(x=0, y=120)

        self.message_text = Text(self, height=10, width=50)

        self.message_text.place(x=58, y=120)

        self.password_label = Label(self, text="Password: ")

        self.password_label.place(x=0, y=300)

        self.password_entry = Entry(self, show='*', font=('Arial', 14))

        self.password_entry.place(x=58, y=300)

        # Initialize speech recognition

        self.r = sr.Recognizer()

        self.microphone = sr.Microphone()

        # Button for speech recognition

        self.speech_button = Button(self, text="Speech Input", command=self.start_speech_recognition)

        self.speech_button.place(x=400, y=0)

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

                self.myemail_entry.delete(0, END)

                self.myemail_entry.insert(END, entry_value)

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

        # Code to send email using the entered values

        pass

    def exit_program(self):

        self.master.destroy()


# Create the Tkinter window

window = Tk()

# Create an instance of the Database_Frame class

frame = DatabaseFrame(window)

# Start the Tkinter event loop

frame.geometry("600x600")

frame.resizable(False, False)

frame.mainloop()
