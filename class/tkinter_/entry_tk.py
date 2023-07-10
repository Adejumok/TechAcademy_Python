from tkinter import *


def dowork():
    print(var.get())


top = Tk()

L1 = Label(top, text='Label')

L1.pack(side=LEFT)

var = StringVar()

E1 = Entry(top, bd=5, textvariable=var)

E1.pack(side=LEFT)

B1 = Button(top, text="Process", command=dowork)

B1.pack()

top.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
#
# window.title("My Window")
#
# window.geometry("500x300")
#
# e1 = tk.Entry(window, show=None)
#
# e2 = tk.Entry(window, show='*', font=('Arial', 14))
#
# e1.pack()
#
# e2.pack()
#
# window.mainloop()
