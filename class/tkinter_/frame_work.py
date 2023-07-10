from tkinter import *

root = Tk()
textLabel = Label(root, text="My Cat", justify=LEFT, padx=10)
textLabel.pack(side=LEFT)
photo = PhotoImage(file="kycservices.jpg")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)
mainloop()
